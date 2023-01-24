import json
from admin_auth import _admin_auth
from helper import get_google_config_dict

def get_groups():
        config_details = get_google_config_dict()
        customer_id = config_details['customer_id'] 
        service = _admin_auth()
        data = []
        response_group = service.groups().list(customer=customer_id).execute()
        
        for group in response_group['groups']:           
            group_key = group['id']
            group_email = group['email']
            group_name = group['name']
            group_description = group['description']
            item = {}
            item[group_email] = [{"group_details":{"group_email": group_email, "group_name": group_name, "group_description": group_description}}]
            group_members = service.members().list(groupKey=group_key).execute()
            _members = []
            if 'members' in group_members:
                for members in group_members['members']:
                    member_email = str(members['email']) if 'email' in members else "No Email"
                    member_status = str(members['status']) if 'status' in members else "No Status"
                    member_role = str(members['role']) if 'role' in members else "No Role"
                    _members.append({"member_email":member_email,"member_status":member_status,"member_role":member_role})
                
                item[group_email].extend(_members)
            else:
                item[group_email] = []
                
            data.append(item)
        jsonDatas=json.dumps(data)
        return(jsonDatas)

if __name__ == '__main__':
    print(get_groups())