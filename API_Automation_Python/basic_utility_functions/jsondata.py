class headerjson:
    validkey = {"Content-Type": 'application/json', "authorization": 'Bearer 1cf30316d82bc319d9499ef27a3450055e2f3450'}
    nvalidkey = {"Content-Type": 'application/json', "authorization": 'Bearer 385b37637d0deff5ffa6494f5c39c7c7e69ec709'}
    noauthtoken = {"Content-Type": 'application/json', "authorization": ''}
    invalidkeyname = {"Content-Type": 'application/json', "auth": 'Bearer e14dd19b09be6e531945f52ff89d599d4008d88b'}
    longstr = 'The Lull Protector has been rigorously tested in four key areas for protection and durability. ' \
              'Stain-Resistant. Protects your mattress from spills & accidents '
    empty_payload = '{}'
    non_english_str = 'El componente geográfico del nombre de este producto es'
    syncuid = '0dd75a90f50b4a56a0361cb5834ea033'
    syncinvaliduid = '0dd75a90f50b4a56a0361cb5834ea088'
    synctestid = "ce1949be-a5a3-42f7-a4a6-a5720ea88be3"
    ivalidsyncorderid = ""
    anothervaliduid = "c0305cf4abff41cca9e1ba78de5f8551"
    viewcarddauth = {"Content-Type": 'application/json', "authorization": "Bearer eyJhbGciOiJSUzUxMiIsImtpZCI6IjEyMzQ1Njc4OTAiLCJ0eXAiOiJKV1QifQ.eyJhcHBfaWQiOjYxNDUsInJldGFpbGVyX2lkIjoyOCwiaXNzIjoia3RwbHRfSldUIiwiZXhwIjoxNjQzMDU2MzYxLCJpYXQiOjE2NDMwNDU1NjEsInNjb3BlIjoidmNjLWp3dC1hcGkvVmlld0NhcmQifQ.hxW0DNBWpq32Rb3xdFnrlW6jrWyLKVrXJz7VyXJsjmfXYx2v7BIcK7yxaePq1XQIquvuVoAveWssbUreK3CW0CyEqBUUrQBc_0cpQScO2hV309Wkj79JhjKlM3pAQ-deTd0L9ECpgVtm-bBD-wCIdPdoXKrC2tA30Rc7IxTyXSBUCulKjc85C--gFtJWUHK3iEicrAN0ZP1JZtD7W0Xdr4wuOXuvnL7Vuxi99_23r3cN0oxzxswRTsneMLM1cuLj8cT90_rXfB9R9XjPO6h4wvH2h_AZvA1ZK_fehO8Mq4TA1tXYZUD4dhanKWKZeVPGQNciJEk9TxzZXHABFey8UeR7VWoiwsKR0N10R0r6h9cQKNnAl7KYTTKGVCdmT8dSfou6HTmZE9DoRk1Te566ifgiewXRINc_i8xj82XN8COjEj-iGwQB3MgjQf4MhdnzFWGjJ_rZxqekeTN195go-t92Yj1Ujz7-3_MO-esrp6jT4iYRH6XX2bKNjnmo3hfWS87wRe_WEMzdJLFv_eBrpWsZv5jpFzlcBFD8Nlzd4ykbNhLHJ6FyMtl-CBKwfPNUQXXZAeaAA7YSobAiqcxmEMecN35yJUfw8cSqgCZ2wx2YAoxbpTpQMN53-uK1VfXDXwkd995idQk3rug3UDrM1E1c7Jn7-HCOne2Hw882BYE"}
    viewcardinvalidauth = {"Content-Type": 'application/json', "authorization": "Bearer eeeyJhbGciOiJSUzUxMiIsImtpZCI6IjEyMzQ1Njc4OTAiLCJ0eXAiOiJKV1QifQ.eyJhcHBfaWQiOjYxMjIsInJldGFpbGVyX2lkIjoyOCwiaXNzIjoia3RwbHRfSldUIiwiZXhwIjoxNjQzMDQ0NTY1LCJpYXQiOjE2NDMwMzM3NjUsInNjb3BlIjoidmNjLWp3dC1hcGkvVmlld0NhcmQifQ.kjQG_JM5b6CiwAns2rSn3J82o6MgiiTF5-vJktOw0zBQjO5aIfj0h2o47q-UzV-4GiUsX2Mz3Xkhhqbk2ammwrjAbMFzMTHjNRB3oDC2_fNgWGj7EkcINaHeB4v5J2alaMSLaOl0RiFQaD_VD0D8-P9W56JZOmesMuWZoPe7aPdMPv0qQPzpJMbJMODNFzEl8hPVuHHfKCJ7zHXEgSzceUyzXrnt6o6zt8xhDBt60hnQ_yuzmVcJGTrixtOfkl9Mc25ld9Kbi1mwjdJlynuVs2WmIlmeFW9l14hQAGWEfO_55jOnEKlPWfFRpfHr7m55Gsvc1Z_LPXlMDkdLT5i9XKvjAztFlUYNgJuE4qE7PvODboXzDZCBjXBe6LERTNUDgNgRd94SeWFU9U26MWYIZUv7VKFpBNog7-kBCsebmczKze1TEu9aANv5UZrqmfrPp5O-sLAwRA1kQO3-1ukrvA9bFRAeYCHnqJxqhY5hqv6UmyQFxRZ9hcL8zzanDN1N6HXgfc4s-qdZqcPD-K3MXMsdyW-Osr5q9RNa0uIPY1zF5mRUq4tC9qjCyxNG6F5ORHH2iBF1F3RCT3nciR00FBgCEDu5iYfaFqCR1XaB08ZefdM4hEURTtZiiH-2Ve137u197SH9ztQIuhbs6bxbIQD1Ogwal9Tjlw1Df9xi2o0"}
    viewcarddauthkeyname = {"Content-Type": 'application/json', "auth": "Bearer eyJhbGciOiJSUzUxMiIsImtpZCI6IjEyMzQ1Njc4OTAiLCJ0eXAiOiJKV1QifQ.eyJhcHBfaWQiOjYxMjIsInJldGFpbGVyX2lkIjoyOCwiaXNzIjoia3RwbHRfSldUIiwiZXhwIjoxNjQzMDQ0NTY1LCJpYXQiOjE2NDMwMzM3NjUsInNjb3BlIjoidmNjLWp3dC1hcGkvVmlld0NhcmQifQ.kjQG_JM5b6CiwAns2rSn3J82o6MgiiTF5-vJktOw0zBQjO5aIfj0h2o47q-UzV-4GiUsX2Mz3Xkhhqbk2ammwrjAbMFzMTHjNRB3oDC2_fNgWGj7EkcINaHeB4v5J2alaMSLaOl0RiFQaD_VD0D8-P9W56JZOmesMuWZoPe7aPdMPv0qQPzpJMbJMODNFzEl8hPVuHHfKCJ7zHXEgSzceUyzXrnt6o6zt8xhDBt60hnQ_yuzmVcJGTrixtOfkl9Mc25ld9Kbi1mwjdJlynuVs2WmIlmeFW9l14hQAGWEfO_55jOnEKlPWfFRpfHr7m55Gsvc1Z_LPXlMDkdLT5i9XKvjAztFlUYNgJuE4qE7PvODboXzDZCBjXBe6LERTNUDgNgRd94SeWFU9U26MWYIZUv7VKFpBNog7-kBCsebmczKze1TEu9aANv5UZrqmfrPp5O-sLAwRA1kQO3-1ukrvA9bFRAeYCHnqJxqhY5hqv6UmyQFxRZ9hcL8zzanDN1N6HXgfc4s-qdZqcPD-K3MXMsdyW-Osr5q9RNa0uIPY1zF5mRUq4tC9qjCyxNG6F5ORHH2iBF1F3RCT3nciR00FBgCEDu5iYfaFqCR1XaB08ZefdM4hEURTtZiiH-2Ve137u197SH9ztQIuhbs6bxbIQD1Ogwal9Tjlw1Df9xi2o0"}
    viewcardauth_as_apikey = {"Content-Type": 'application/json', "authorization": "Bearer 1cf30316d82bc319d9499ef27a3450055e2f3450"}
    viewcard_noauth = {"Content-Type": 'application/json', "authorization": ""}


class filepath:
    leasable_file_path = '../files_to_access/ab_leasable.csv'
    retailer_info_filepath = '../files_to_access/retailer_publicKey.csv'
    writefilepath = '../files_to_access/newfile.csv'
    specialcharfilepath = '../files_to_access/special_char.csv'
    write_to_file = '../files_to_access/response.csv'


