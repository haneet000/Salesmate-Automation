import json


def main_url_payload():
    main_payload = json.dumps({
        "fields": [
            "deal.primaryContact.name",
            "deal.primaryCompany.name",
            "deal.primaryContact.mobile",
            "deal.lastActivityAt",
            "deal.lastNote",
            "deal.textCustomField7",
            "deal.description",
            "deal.intCustomField1",
            "deal.dateTimeCustomField1",
            "deal.textCustomField11",
            "deal.title",
            "deal.pipeline",
            "deal.dealValue",
            "deal.estimatedCloseDate",
            "deal.status",
            "deal.currency",
            "deal.stage",
            "deal.primaryContact.id",
            "deal.primaryContact.email",
            "deal.primaryCompany.id",
            "deal.owner.name",
            "deal.winProbability",
            "deal.lostReason",
            "deal.lastCommunicationAt",
            "deal.primaryContact.phone"
        ],
        "query": {
            "group": {
                "operator": "AND",
                "rules": [
                    {
                        "condition": "EQUALS",
                        "data": {
                            "group": "Surepass",
                            "value": "Initalized"
                        },
                        "field": {
                            "fieldName": "deal.pipeline",
                            "displayName": "Pipeline",
                            "type": "Select"
                        }
                    },
                    {
                        "group": {
                            "operator": "AND",
                            "rules": [
                                {
                                    "condition": "EQUALS",
                                    "data": "Open",
                                    "eventType": "Select",
                                    "field": {
                                        "fieldName": "deal.status"
                                    },
                                    "moduleName": "Deal",
                                    "selectedObject": ""
                                },
                                {
                                    "condition": "NOT_EQUALS",
                                    "data": [
                                       Peraon data 
                                    ],
                                    "eventType": "Tag",
                                    "field": {
                                        "fieldName": "deal.tags"
                                    },
                                    "moduleName": "Deal",
                                    "selectedObject": ""
                                }
                            ]
                        }
                    }
                ]
            }
        },
        "sortBy": {
            "fieldName": "deal.createdAt",
            "order": "desc"
        }
    })
    return main_payload


def find_uan(status_response):
    find_url_payload = json.dumps({
        "mobile_number": status_response
    })
