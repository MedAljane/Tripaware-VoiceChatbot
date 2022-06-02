def sortKey(e):
    return e["TotalPrice"]

def classifyByCarrier(js):
    carriersDict = {}
    multipleStops = False

    if type(js[0]["Details"]) == list and len(js[0]["Details"]) != 1:
        multipleStops = True

    if type(js[0]["Details"]) == list:
        if multipleStops and js[0]["Details"][0]["type"] != "walk":
            carriersList = list(set([el["Details"][0]["companyName"] for el in js]))

        elif not multipleStops and js[0]["Details"][0]["type"] == "navette":
            carriersList = list(set([el["Details"][0]["companyName"] for el in js]))

        elif multipleStops:
            for el in js:
                compNamesInDetails = {}
                for detail in el["Details"]:
                    if detail["type"] == "walk":
                        pass
                    else:
                        if detail["companyName"] in compNamesInDetails.keys():
                            compNamesInDetails["companyName"] += 1
                        else:
                            compNamesInDetails["companyName"] = 1
                
                carriersList.append(compNamesInDetails.get(max(compNamesInDetails.values())))
            carriersList = list(set(carriersList))
    
    elif type(js[0]["Details"]) == dict:
        carriersList = list(set([el["Details"]["companyName"] for el in js]))
    else:
        print("Error while sorting!")
        print(js)
        return False
        
    print("Carriers list:", carriersList)

    if multipleStops:
        for carrier in carriersList:
            carrierDetails = [e for e in js if e["Details"][0]["companyName"] == carrier]
            carrierDetails.sort(key=sortKey)
            carriersDict[carrier] = carrierDetails
            
    else:
        for carrier in carriersList:
            carrierDetails = [e for e in js if e["Details"]["companyName"] == carrier]
            carrierDetails.sort(key=sortKey)
            carriersDict[carrier] = carrierDetails
        
    return {"Carriers":carriersDict, "MultipleStops": multipleStops}