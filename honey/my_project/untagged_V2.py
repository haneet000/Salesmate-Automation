import requests
import json
from honey.my_project.untagged_leads_uan_history_payload import main_url_payload
import traceback

class Uan_history_untagged():
    def __init__(self):
        self.email_id_response = None
        self.html_full_name = None
        self.html_content = None
        self.lead_note_console = None
        self.last_10_digits = None
        self.all_get_data = []
        self.list_to_json = {}
        self.session = requests.session()
        self.index = 0
        self.lead_id = None
        # fetch data down arrow side
        self.main_url = "https://surepass.salesmate.io/apis/deal/v1/board-view/cards?rows=68&from=0"
        self.find_uan_url = "https://sandbox.surepass.io/api/v1/income/epfo/find-uan"
        self.uan_history_url = "https://sandbox.surepass.io/api/v1/income/employment-history-uan"
        self.phone_to_full_name = "https://kyc-api.surepass.io/api/v1/bank-verification/upi-mobile-to-name"
        self.email_logs_url = "https://app.surepass.io/api/v1/admin/email-logs"
        self.salemate_id_to_console_url = "https://app.surepass.io/api/v1/admin/set-crm-profile-url"
        self.phone_number_verification_url = "https://sandbox.aadhaarapi.io/api/v1/telecom/telecom-verification"

    main_url_headers = {
        'authority': 'surepass.salesmate.io',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'accesstoken': '6ec46a30-5c27-11ee-8633-f131abf1e8e3-c5922af8-1f12-4b87-8a34-725e09255644',
        'content-type': 'application/json',
        'cookie': '_fbp=fb.1.1691751413434.1501901083; sm-hn=surepass.salesmate.io; sm-ac-tk=6ec46a30-5c27-11ee-8633-f131abf1e8e3-c5922af8-1f12-4b87-8a34-725e09255644; sm-user-email=sales%40surepass.io; sm-impersonate=false; sm-is-login-using-recovery-code=false; sm-user-id=7; sm-hn-common=surepass.salesmate.io; amp_6e403e=7zlkwpITU9i3S_X2-EJ-m9...1hf70bua7.1hf70bua7.d.0.d; landedOnPage=www.salesmate.io; _hjSessionUser_1217448=eyJpZCI6ImUyYTc3ODA3LWZlY2ItNTg4ZS1iZWJlLTBhZjY2OGYxMjQ1ZSIsImNyZWF0ZWQiOjE3MDM4NDM2NTgzMDYsImV4aXN0aW5nIjp0cnVlfQ==; _gcl_au=1.1.422296213.1703843659; utm_source=Direct; utm_medium=(Direct); _clck=4w4ks9%7C2%7Cfjh%7C0%7C1458; _ga=GA1.1.528073730.1664513486; _ga_0LEBD9YWK3=GS1.1.1708686485.22.0.1708686488.57.0.0; sm-container-state=true',
        'isimpersonate': 'false',
        'origin': 'https://surepass.salesmate.io',
        'referer': 'https://surepass.salesmate.io/',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'x-linkname': 'surepass.salesmate.io',
        'x-workspace-id': ''
    }

    lead_header = {
        'authority': 'surepass.salesmate.io',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'accesstoken': '6ec46a30-5c27-11ee-8633-f131abf1e8e3-c5922af8-1f12-4b87-8a34-725e09255644',
        'content-type': 'application/json',
        'cookie': '_fbp=fb.1.1691751413434.1501901083; sm-hn=surepass.salesmate.io; sm-ac-tk=6ec46a30-5c27-11ee-8633-f131abf1e8e3-c5922af8-1f12-4b87-8a34-725e09255644; sm-user-email=sales%40surepass.io; sm-impersonate=false; sm-is-login-using-recovery-code=false; sm-user-id=7; sm-hn-common=surepass.salesmate.io; amp_6e403e=7zlkwpITU9i3S_X2-EJ-m9...1hf70bua7.1hf70bua7.d.0.d; landedOnPage=www.salesmate.io; _hjSessionUser_1217448=eyJpZCI6ImUyYTc3ODA3LWZlY2ItNTg4ZS1iZWJlLTBhZjY2OGYxMjQ1ZSIsImNyZWF0ZWQiOjE3MDM4NDM2NTgzMDYsImV4aXN0aW5nIjp0cnVlfQ==; _gcl_au=1.1.422296213.1703843659; utm_source=Direct; utm_medium=(Direct); _clck=4w4ks9%7C2%7Cfjh%7C0%7C1458; _gid=GA1.2.721485861.1708583433; _ga=GA1.2.528073730.1664513486; _clsk=r4lhoj%7C1708583455759%7C2%7C1%7Cz.clarity.ms%2Fcollect; _ga_0LEBD9YWK3=GS1.1.1708583432.21.1.1708583459.33.0.0; sm-container-state=true',
        'isimpersonate': 'false',
        'origin': 'https://surepass.salesmate.io',
        'referer': 'https://surepass.salesmate.io/',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'x-linkname': 'surepass.salesmate.io',
        'x-workspace-id': ''
    }

    salemate_id_to_console_headers = {
          'authority': 'app.surepass.io',
          'accept': 'application/json, text/plain, */*',
          'accept-language': 'en-US,en;q=0.9',
          'content-type': 'application/json',
          'cookie': 'sib_cuid=79a397ff-3504-4c4b-8e93-52299c2cdad5; _gcl_au=1.1.1151342286.1707566274; _ga=GA1.1.819824749.1707566274; messagesUtk=59de5c0ecd8e4c1199abd3a52d09f504; _hjSessionUser_2837838=eyJpZCI6ImYwMGNiMDI5LTRjYzQtNWQ5Yy1hYTA5LWQ0MjIyMGJiNmZiOSIsImNyZWF0ZWQiOjE3MDc1NjY0MTYzMTAsImV4aXN0aW5nIjp0cnVlfQ==; ajs_anonymous_id=%225c897b5d-47b7-4587-b067-475f8e81610c%22; hubspotutk=e1e1bb92912b4f2c9fd1402a40942aef; GCP_IAP_UID=117281239643461000806; cf_clearance=WOvfHkXht5SA2P0cojmiLSLbddoEeun3bvZYVJBEugw-1709552738-1.0.1.1-ZwvztLQd.8Ihmwlnb7YA1QCT9aIff7sRJJ4ZrF53gst46vYI7aDdluzmDlDPh71.gyIO4cH3FzrTMBsOc_LgEw; __hstc=190410484.e1e1bb92912b4f2c9fd1402a40942aef.1707566865768.1707566865768.1709552738098.2; _ga_XTFP6C19HL=GS1.1.1709552734.2.1.1709553783.0.0.0; access-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDk4Mzc3ODEsInN1YiI6ImhhbmVldHNpbmdoLnN1cmVwYXNzQGdtYWlsLmNvbSIsInNjb3BlcyI6bnVsbCwidHlwZSI6ImFjY2VzcyJ9.XIb37TjeIqhDnjbUGMkRnVg1R4K6WeQ3MyXbJwVctz8; refresh-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTI0MDgxODEsInN1YiI6ImhhbmVldHNpbmdoLnN1cmVwYXNzQGdtYWlsLmNvbSIsInNjb3BlcyI6bnVsbCwidHlwZSI6InJlZnJlc2gifQ.-EsY4rT6dCIa9T3eM6FYdL6uG52zvy_HnkEOLJ97kNg',
          'origin': 'https://console-admin.surepass.io',
          'referer': 'https://console-admin.surepass.io/',
          'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
          'sec-fetch-dest': 'empty',
          'sec-fetch-mode': 'cors',
          'sec-fetch-site': 'same-site',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
        }
    email_logs_headers = {
        'authority': 'app.surepass.io',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'cookie': 'sib_cuid=79a397ff-3504-4c4b-8e93-52299c2cdad5; _gcl_au=1.1.1151342286.1707566274; _ga=GA1.1.819824749.1707566274; messagesUtk=59de5c0ecd8e4c1199abd3a52d09f504; _hjSessionUser_2837838=eyJpZCI6ImYwMGNiMDI5LTRjYzQtNWQ5Yy1hYTA5LWQ0MjIyMGJiNmZiOSIsImNyZWF0ZWQiOjE3MDc1NjY0MTYzMTAsImV4aXN0aW5nIjp0cnVlfQ==; ajs_anonymous_id=%225c897b5d-47b7-4587-b067-475f8e81610c%22; __hstc=190410484.e1e1bb92912b4f2c9fd1402a40942aef.1707566865768.1707566865768.1707566865768.1; hubspotutk=e1e1bb92912b4f2c9fd1402a40942aef; GCP_IAP_UID=117281239643461000806; _ga_XTFP6C19HL=GS1.1.1707566273.1.1.1707567614.0.0.0; cf_clearance=TaIe6_Nf0ja3IPU2uydFav5rm8CmrGHjMwn_lccn1lk-1709366012-1.0.1.1-si5a8LWEp3kftjN1jGvR9fI5PIYysxSE74qvSMt7.JOCLWiZo5boxjRn2JH0dboXz3Tx.VHmcrDWmaBYNUAc6A; access-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDk1NTM4MTQsInN1YiI6ImhhbmVldHNpbmdoLnN1cmVwYXNzQGdtYWlsLmNvbSIsInNjb3BlcyI6bnVsbCwidHlwZSI6ImFjY2VzcyJ9.HeRg3M79bnWaHhl6esZeotLKnkjjSjdYaT3r2EBe5rc; refresh-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTIxMjQyMTQsInN1YiI6ImhhbmVldHNpbmdoLnN1cmVwYXNzQGdtYWlsLmNvbSIsInNjb3BlcyI6bnVsbCwidHlwZSI6InJlZnJlc2gifQ.qe0L_zpRZGpcYya1yFeEktovIHLH5NCgSSUGXF-JBiU',
        'origin': 'https://console-admin.surepass.io',
        'referer': 'https://console-admin.surepass.io/',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
    }

    email_id_logs_headers = {
          'authority': 'app.surepass.io',
          'accept': 'application/json, text/plain, */*',
          'accept-language': 'en-US,en;q=0.9',
          'cookie': 'sib_cuid=79a397ff-3504-4c4b-8e93-52299c2cdad5; _gcl_au=1.1.1151342286.1707566274; _ga=GA1.1.819824749.1707566274; messagesUtk=59de5c0ecd8e4c1199abd3a52d09f504; _hjSessionUser_2837838=eyJpZCI6ImYwMGNiMDI5LTRjYzQtNWQ5Yy1hYTA5LWQ0MjIyMGJiNmZiOSIsImNyZWF0ZWQiOjE3MDc1NjY0MTYzMTAsImV4aXN0aW5nIjp0cnVlfQ==; ajs_anonymous_id=%225c897b5d-47b7-4587-b067-475f8e81610c%22; hubspotutk=e1e1bb92912b4f2c9fd1402a40942aef; GCP_IAP_UID=117281239643461000806; cf_clearance=WOvfHkXht5SA2P0cojmiLSLbddoEeun3bvZYVJBEugw-1709552738-1.0.1.1-ZwvztLQd.8Ihmwlnb7YA1QCT9aIff7sRJJ4ZrF53gst46vYI7aDdluzmDlDPh71.gyIO4cH3FzrTMBsOc_LgEw; __hstc=190410484.e1e1bb92912b4f2c9fd1402a40942aef.1707566865768.1707566865768.1709552738098.2; _ga_XTFP6C19HL=GS1.1.1709552734.2.1.1709553783.0.0.0; access-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTAxMTYyOTcsInN1YiI6ImhhbmVldHNpbmdoLnN1cmVwYXNzQGdtYWlsLmNvbSIsInNjb3BlcyI6bnVsbCwidHlwZSI6ImFjY2VzcyJ9.7RiowzmaNKpF9kZfyG1QThtmxWc0tjMasoEIijXCVOU; refresh-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTI2ODY2OTcsInN1YiI6ImhhbmVldHNpbmdoLnN1cmVwYXNzQGdtYWlsLmNvbSIsInNjb3BlcyI6bnVsbCwidHlwZSI6InJlZnJlc2gifQ.z6ayHXFwmYMEopD32_JVLXO5fMyzagSh6N91-oPkRps',
          'origin': 'https://console-admin.surepass.io',
          'referer': 'https://console-admin.surepass.io/',
          'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Windows"',
          'sec-fetch-dest': 'empty',
          'sec-fetch-mode': 'cors',
          'sec-fetch-site': 'same-site',
          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
        }

    uan_header = {
        'Authorization': 'Bearer Add your token',
        'Content-Type': 'application/json'
    }

    phone_to_full_name_headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer Add your token
    }

    main_payload = main_url_payload()

    def main_url_func(self):
        try:
            while True:
                response = self.session.post(self.main_url, headers=self.main_url_headers, data=self.main_payload)
                request_response = response.json()
                if len(request_response['Data']['data']) <= self.index:
                    print("No more leads to process.")
                    break

                lead_data = request_response['Data']['data'][self.index]['primaryContact']
                phone_number_id_response = lead_data.get('mobile')
                self.email_id_response = lead_data.get('email')
                self.lead_id = request_response['Data']['data'][self.index]['id']

                if phone_number_id_response:
                    self.last_10_digits = phone_number_id_response[-10:]
                    print(self.last_10_digits, self.email_id_response)
                    self.console_to_salemate()

        except Exception as e:
            print(f"An error occurred in main_url_func: {e}")
            traceback.print_exc()

    def console_to_salemate(self):
        try:
            email_logs_url = f"https://app.surepass.io/api/v1/admin/get-target-user-profile?target_user_email={self.email_id_response}"
            print(email_logs_url)

            email_log_response = self.session.get(email_logs_url, headers=self.email_id_logs_headers)
            if email_log_response.status_code == 200:
                self.lead_note_console = f"<div>Console - https://console-admin.surepass.io/self-signup/profile/{self.email_id_response}</div>"
                self.find_email_to_phone()
            else:
                self.lead_note_console = "<div>Console Not Available</div>"
                self.find_email_to_phone()

        except Exception as e:
            print(f"An error occurred in console_to_salemate: {e}")
            traceback.print_exc()

    def find_email_to_phone(self):
        try:
            phone_number_verification_payload = json.dumps({"id_number": self.last_10_digits})
            phone_number_verification = self.session.post(self.phone_number_verification_url, headers=self.uan_header,
                                                          data=phone_number_verification_payload)

            if phone_number_verification.status_code == 200:
                find_phone_to_name_payload = json.dumps({"mobile_number": self.last_10_digits})
                find_phone_to_name_response = self.session.post(self.phone_to_full_name,
                                                                headers=self.phone_to_full_name_headers,
                                                                data=find_phone_to_name_payload)

                if find_phone_to_name_response.status_code == 200:
                    find_email_to_phone_data = find_phone_to_name_response.json().get('data', {})
                    full_name_response = find_email_to_phone_data.get('full_name')
                    print(f"Email to phone successfully found {full_name_response}")
                    self.html_full_name = f"<div><p>Full Name: {full_name_response}</p><br></div>"
                    self.find_uan()
                else:
                    print(
                        f"Failed to retrieve email to phone. Response status: {find_phone_to_name_response.status_code}")
                    self.html_full_name = "<div><p>Full Name: Not Available</p><br></div>"
                    self.find_uan()
            else:
                print('Phone number verification 422')
                self.html_full_name = "<div><p>Full Name: Not Available</p><br></div>"
                self.html_content = "<div><p>Uan History : Not Available</p><br></div>"
                self.make_lead()

        except Exception as e:
            print(f"An error occurred in find_email_to_phone: {e}")
            traceback.print_exc()

    def find_uan(self):
        try:
            find_uan_payload = json.dumps({"mobile_number": self.last_10_digits})
            find_uan_response = self.session.post(self.find_uan_url, headers=self.uan_header, data=find_uan_payload)

            if find_uan_response.status_code == 200:
                pf_number = find_uan_response.json()['data']['pf_uan']
                print(pf_number)
                id_number_payload = json.dumps({"id_number": pf_number})
                uan_history_response = self.session.post(self.uan_history_url, headers=self.uan_header,data=id_number_payload)
                uan_history_response_json = uan_history_response.json()
                employment_history = uan_history_response_json.get('data', {}).get('employment_history', [])

                if employment_history:
                    self.html_content = "<div>"
                    for entry in employment_history:
                        entry_html = f"""
                                            <p>Name: {entry['name']}</p>
                                            <p>Guardian Name: {entry['guardian_name']}</p>
                                            <p>Establishment Name: {entry['establishment_name']}</p>
                                            <p>Member ID: {entry['member_id']}</p>
                                            <p>Date of Joining: {entry['date_of_joining']}</p>
                                            <p>Date of Exit: {entry['date_of_exit']}</p>
                                            <br>
                                        """
                        self.html_content += entry_html
                    self.html_content += "</div>"
                    self.make_lead()
                else:
                    self.html_content = "<div> Uan History not available <div>"
                    self.make_lead()

        except Exception as e:
            print(f"An error occurred in find_uan: {e}")
            traceback.print_exc()

    def make_lead(self):
        try:
            lead_url = f"https://surepass.salesmate.io/apis/deal/v4/modules/4/object/{self.lead_id}/notes"
            main_note = f"<div>{self.html_full_name}</div><div>{self.html_content}</div><div>{self.lead_note_console}</div>"
            print(main_note)
            lead_id_payload = json.dumps({
                "note": main_note,
                "attachments": [],
                "type": "Note"
            })

            lead_id_response = self.session.post(lead_url, headers=self.lead_header, data=lead_id_payload)
            print(lead_id_response.status_code)

            salemates_id_to_console_payload = json.dumps({"target_user_email": self.email_id_response,
                                                          "crm_profile_url": f'https://surepass.salesmate.io/#/app/deals/{self.lead_id}/detail'})
            salemate_id_to_console_res = self.session.post(self.salemate_id_to_console_url,
                                                           headers=self.salemate_id_to_console_headers,
                                                           data=salemates_id_to_console_payload)
            print(f'{salemate_id_to_console_res.status_code} Salemate link added on console')
            self.index += 1

        except Exception as e:
            print(f"An error occurred in make_lead: {e}")
            traceback.print_exc()


if __name__ == "__main__":
    lead_processor = Uan_history_untagged()
    lead_processor.main_url_func()
