import csv
from requests import HTTPError as errors
from admin_auth import _admin_auth
from helper import get_google_config_dict


directory_service = _admin_auth()
config_details = get_google_config_dict()
customer_id = config_details['customer_id']
all_groups = []
all_members = []
page_token = None
new_page_token = None
params = {'customer': customer_id}
data_list = []

while True:
  try:
    if page_token:
      params['pageToken'] = page_token
    current_page = directory_service.groups().list(**params).execute()

    all_groups.extend(current_page['groups'])
    page_token = current_page.get('nextPageToken')
    if not page_token:
      break
  except errors.HttpError as error:
    print('An error occurred: %s' % error)
    break

for group in all_groups:
  group_key = group['email']
  new_params = {'groupKey': '%s' % group_key, 'maxResults': '500'}

  if group['directMembersCount'] == '0':
    continue
  else:
    while True:
      try:
        if new_page_token:
          new_params['pageToken'] = new_page_token
        new_current_page = directory_service.members().list(**new_params).execute()
        all_members.extend(new_current_page['members'])
        new_page_token = new_current_page.get('nextPageToken')

        if not new_page_token:
          break
      except errors.HttpError as error:
        print('An error occurred: %s' % error)
        break

  
  for member in all_members:
    if 'email' in member:
      row = group['email'],group['name'],group['description'],member['email'],member['role']
      data_list.extend([row])
    else:
      row = group['email'],group['name'],group['description'],'NO EMAIL',member['role']
      data_list.extend([row])
  del all_members[:]

with open("Output.csv", "w", newline="") as Output_File:
  writer = csv.writer(Output_File,quotechar='|', quoting=csv.QUOTE_MINIMAL)
  writer.writerow(['Group Email','Group Name','Group Description','Member Email','Member Role'])
  writer.writerows(data_list)
