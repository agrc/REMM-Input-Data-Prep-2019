print "importing arcpy module"
import arcpy
arcpy.env.workspace= "T:\_2REMM\BaseYear2019\Parcel Checks 2020\Parcel Checks 2020\Parcel Checks 2020.gdb"
featureclasslist= arcpy.ListFeatureClasses()
#importing files and geodatabases onto python library script arcpy.
#Using four different attributes to make pattern distinctions
#Property type user description (USEDSCRP),
#tax account type(TXACCTTYPE),
#Class description (CLASSDSCRP),
#property type description (PROP_TYPECDDSCRP).

file ="Parcles_Utah_20202503"
rows = arcpy.UpdateCursor(file)
for row in rows:
    if row.USEDSCRP == "SINGLE FAMILY RES":
        if row.TXACCTTYPE == "HGH DEN RES":
            row.building_type_id = 2
        elif row.TXACCTTYPE == "RESIDENTIAL":
            if row.CLASSDSCRP == "None":       
                row.building_type_id = 1
            elif (row.CLASSDSCRP == "MANUFACTURED HOME") or (row.CLASSDSCRP == "Manufactured Home"):
                if row.PROP_TYPECDDSCRP == "M/H AFFIXED > 1 ACRE" or row.PROP_TYPECDDSCRP == "RESIDENTIAL-SINGLE > 1 ACRE":
                    row.building_type_id = 2
                else:
                    row.building_type_id = 7
            elif row.CLASSDSCRP == "Manufactured Home":
                row.building_type_id = 2
            elif row.CLASSDSCRP == "Modular Home":
                if row.PROP_TYPECDDSCRP == "MULTIPLE RES + AG > 1 ACRE":
                    row.building_type_id = 7
                else:
                    row.building_type_id = 1
            elif row.CLASSDSCRP == "Single Family Res":
                if row.PROP_TYPECDDSCRP == "MULTIPLE RES + AG > 1 ACRE":
                    row.building_type_id = 7
                else:
                    row.building_type_id = 1
      
    if row.USEDSCRP == "APARTMENTS":
        row.building_type_id = 2

    elif row.USEDSCRP == "CONDO":
        row.building_type_id = 2

    elif row.USEDSCRP == "DUPLEX":
        row.building_type_id = 2

    elif row.USEDSCRP == "FOURPLEX":
         row.building_type_id = 2

    elif row.USEDSCRP == "PUD":
        if row.TXACCTTYPE == "RESIDENTIAL":
               row.building_type_id = 1
        elif row.TXACCTTYPE == "APARTMENTS":
               row.building_type_id = 12
        elif row.TXACCTTYPE == "HGH DEN RES":
            if (row.CLASSDSCRP == "Townhome") or (row.CLASSDSCRP == "Twin Home"):
                row.building_type_id = 2
            elif row.CLASSDSCRP == "Detached Twin Home":
                if row.PROP_TYPECDDSCRP == "RESIDENTIAL TWIN HOME":
                    row.building_type_id = 2
                else:
                    row.building_type_id = 1
                    
    elif row.USEDSCRP == "TRIPLEX":
        row.building_type_id = 2

    elif row.USEDSCRP == "VACANT APARTMENT":
        if row.TXACCTTYPE == "APARTMENTS":
            if row.CLASSDSCRP == "Res Adjoining":
                row.building_type_id = 12
            else:
                row.building_type_id = 2

    elif row.USEDSCRP == "VACANT COMMERCIAL":
        if row.TXACCTTYPE == "EXEMPT":
             row.building_type_id = 12
        elif row.TXACCTTYPE == "COMMERCIAL":
            if row.CLASSDSCRP == "Salvage Imp":
                row.building_type_id = 8
            elif row.CLASSDSCRP == "Vac Comm w/ Det Struct" or row.CLASSDSCRP == "Unbuildable Com w/Det":
                row.building_type_id = 12
            
        
    elif row.USEDSCRP == "MANUFACTURED HOME-SKIRTING":
        if row.TXACCTTYPE == "RESIDENTIAL":
            if row.CLASSDSCRP == "Manufactured Home":
                row.building_type_id = 2
            elif row.CLASSDSCRP == "Vac Sub Lot w/ Det Struct":
                if row.PROP_TYPECDDSCRP == "M/H PERS PROP":
                    row.building_type_id = 2
                else:
                    row.building_type_id = 7

    elif row.USEDSCRP == "MOBILE HOME-SKIRTING":
        if row.TXACCTTYPE == "RESIDENTIAL":
            if (row.CLASSDSCRP == "None") or (row.CLASSDSCRP == "<Null>"):
                if row.PROP_TYPECDDSCRP == "MULTIPLE, M/H + AG > 1 ACRE":
                    row.building_type_id = 7
                else:
                    row.building_type_id = 2

    elif row.USEDSCRP == "TRAILER PARK":
        row.building_type_id = 2

    elif row.USEDSCRP == "SUBSIDIZE HOUSING":
        if row.TXACCTTYPE == "APARTMENTS" or row.TXACCTTYPE == "HGH DEN RES":
            row.building_type_id = 2
        else:
            row.building_type_id = 11

    elif row.USEDSCRP == "STUDENT HOUSING":
        row.building_type_id = 11

    elif row.USEDSCRP == "RES CONVERSION TO APT":
        if row.TXACCTTYPE == "APARTMENTS":
            row.building_type_id = 2
        else:
            row.building_type_id = 1

    elif row.USEDSCRP == "MULTIPLE UNIT MIX":
        if row.TXACCTTYPE == "APARTMENTS":
            if row.CLASSDSCRP == "Multiple Unit Mix":
                row.building_type_id = 2
            else:
                row.building_type_id = 1

    elif row.USEDSCRP == "MULTIPLE RES":
        if row.TXACCTTYPE == "RESIDENTIAL":
            if row.CLASSDSCRP == "Multiple Res":
                if row.PROP_TYPECDDSCRP == "MULTIPLE RES + AG > 1 ACRE":
                    row.building_type_id = 7
                elif row.PROP_TYPECDDSCRP == "RESIDENTIAL + M/H":
                    row.building_type_id =  2
                elif row.PROP_TYPECDDSCRP == "SECONDARY RESIDENTIAL":
                    row.building_type_id = 8
                else:
                    row.building_type_id = 1
                   
    elif row.USEDSCRP == "Privilege Tax On Part exempt":
        row.building_type_id = 8

    elif row.USEDSCRP == "PARTIALLY EXEMPT COUNTY":
        if row.TXACCTTYPE == "EXEMPT":
            row.building_type_id = 8
        elif row.TXACCTTYPE == "COMMERCIAL":
            if row.CLASSDSCRP == "Parking Structure":
                row.building_type_id = 12
            elif row.CLASSDSCRP == "Lt Ind - Whse - Flex Bldg":
                row.building_type_id = 3
            elif row.CLASSDSCRP == "Vac Comm w/ Det Struct":
                row.building_type_id = 9
            else:
                row.building_type_id = 13
    elif row.USEDSCRP == "PARTIAL EXEMPT-Clarissa":
        if row.TXACCTTYPE == "COMMERCIAL":
            if row.CLASSDSCRP == "Lt Ind - Whse - Flex Bldg" or row.CLASSDSCRP == "Unbuildable Com lot":
                row.building_type_id = 3
            elif row.TXACCTTYPE == "RESIDENTIAL":
                row.building_type_id = 9
            elif row.CLASSDSCRP == "Single Family Res":
                row.building_type_id = 1

    elif row.USEDSCRP == "IMPROVED CONDOS":
        if row.TXACCTTYPE == "COMMERCIAL":
            if row.CLASSDSCRP == "Bank" or row.CLASSDSCRP == "Garage-Mini-Lube-Storage Gar":
                row.building_type_id = 8
            elif row.CLASSDSCRP == "Parking Structure" or row.CLASSDSCRP == "Banquet-Pavilion-Club":
                row.building_type_id = 12
            elif row.CLASSDSCRP == "Medical Office":
                row.building_type_id =  5
            elif row.CLASSDSCRP == "Lt Ind - Whse - Flex Bldg":
                row.building_type_id = 3
            elif row.CLASSDSCRP == "Shell - All":
                row.building_type_id =  7
            else:
                row.building_type_id = 4
    
    elif row.USEDSCRP == "IMPROVED PUD":
        if row.TXACCTTYPE == "EXEMPT":
            row.building_type_id =  5
        elif row.TXACCTTYPE == "COMMERCIAL":
            if row.CLASSDSCRP == "Medical Office" or row.CLASSDSCRP == "Specialized":
                row.building_type_id =  5
            elif row.CLASSDSCRP == "Bank" or row.CLASSDSCRP == "Banquet-Pavilion-Club" or row.CLASSDSCRP == "Garage-Mini-Lube-Storage Gar":
                row.building_type_id = 8
            elif row.CLASSDSCRP == "Shell - All":
                row.building_type_id = 7
            elif row.CLASSDSCRP == "No Bldg" or row.CLASSDSCRP == "Lt Ind - Whse - Flex Bldg":
                row.building_type_id = 3
            else:
                row.building_type_id = 4
      
    elif row.USEDSCRP == "COMMERCIAL WITH RES EXEMPTION":
        if row.TXACCTTYPE == "COMMERCIAL":
            if row.CLASSDSCRP == "Single Family Res":
                row.building_type_id =  2
            elif row.CLASSDSCRP == "Banquet-Pavilion-Club":
                row.building_type_id =  12
            elif row.CLASSDSCRP == "Group Care-Nrsg-Retire-Res Prim":
                if row.PROP_TYPECDDSCRP == "RESIDENTIAL NURSING HOME":
                    row.building_type_id =  11
                else:
                    row.building_type_id = 7

    elif row.USEDSCRP == "MIXED USE":
        if row.TXACCTTYPE == "EXEMPT":
            if row.CLASSDSCRP == "Banquet-Pavilion-Club":
                row.building_type_id = 7
            elif row.CLASSDSCRP == "School - Church":
                row.building_type_id = 10
        elif row.TXACCTTYPE == "APARTMENTS":
            row.building_type_id = 7
        elif row.TXACCTTYPE == "COMMERCIAL":
            if (row.CLASSDSCRP == "Airport Hangar")  or (row.CLASSDSCRP == "Medical office") or (row.CLASSDSCRP == "Retail - Discount - Market") or (row.CLASSDSCRP == "Banquet-Pavilion-Club"):
                row.building_type_id = 8
            elif row.CLASSDSCRP == "Group Care-Nrsg-Retire-Res Prim":
                row.building_type_id =  11
            elif row.CLASSDSCRP == "Restaurant - Fast Food":
                row.building_type_id = 4
            elif row.CLASSDSCRP == "Lt Ind - Whse - Flex Bldg":
                row.building_type_id = 3
            elif row.CLASSDSCRP == "Specialized" or (row.CLASSDSCRP == "Garage-Mini-Lube-Storage Gar"):
                row.building_type_id = 7
            elif row.CLASSDSCRP == "School - Church":
                row.building_type_id = 9
            elif row.CLASSDSCRP == "Lt Ind - Whse - Flex Bldg":
                if row.PROP_TYPECDDSCRP == "COMM-INDUSTRIAL":
                    row.building_type_id = 3
            elif row.CLASSDSCRP == "Trailer Park":
                if row.PROP_TYPECDDSCRP == "MULTI, M/H, AG & COMM":
                    row.building_type_id = 2
                else:
                    row.building_type_id = 7 
     
    elif row.USEDSCRP == "COMMERCIAL":
        if row.TXACCTTYPE == "EXEMPT":
            if row.CLASSDSCRP == "None":
                row.building_type_id = 11
            elif row.CLASSDSCRP == "Lt Ind - Whse - Flex Bldg":
                row.building_type_id = 3
            else:
                row.building_type_id = 8
        elif row.TXACCTTYPE == "COMMERCIAL":
            if row.CLASSDSCRP == "Medical Office":
                row.building_type_id = 5
            elif row.CLASSDSCRP == "None":
                row.building_type_id = 11
            elif row.CLASSDSCRP == "Auto Dealer-Used Car Lot-Srvc Ctr" or row.CLASSDSCRP == "Conv Store-Srvc Station-Mini-Mart" or row.CLASSDSCRP == "Hotel - Motel - Lodge":
                 row.building_type_id = 4
            elif row.CLASSDSCRP == "Hospital-Outpatient Surg Ctr":
                 row.building_type_id =13
            elif (row.CLASSDSCRP == "School - Church"): 
                 row.building_type_id = 9
            elif (row.CLASSDSCRP == "Retail - Discount - Market") or (row.CLASSDSCRP == "Restaurant - Fast Food") or (row.CLASSDSCRP == "Shopping Center"):
                 row.building_type_id = 4
            elif row.CLASSDSCRP == "Group Care-Nrsg-Retire-Res Prim":
                if row.PROP_TYPECDDSCRP == "COMM NURSING HOME":
                     row.building_type_id =11
                elif row.PROP_TYPECDDSCRP == "AG-COMM BLDGS":
                     row.building_type_id = 7
                elif row.PROP_TYPECDDSCRP ==  "COMM-FOOD":
                     row.building_type_id = 4
                else:
                    row.building_type_id = 7 
            elif row.CLASSDSCRP == "Lt Ind - Whse - Flex Bldg" or row.CLASSDSCRP == "Greenhouse":
                row.building_type_id = 3
            else:
                row.building_type_id = 8

     #Anything else that needs to be accounted for that wasn't mentioned on the list prior
     # Schools, churches, anything else that was not captured on the list above   

    if (row.USEDSCRP == "EXEMPT") and (row.COMMONAREA == "Yes"):
        row.building_type_id = 12
    if row.PRIVATEROAD == "Yes":
        row.building_type_id = 12
    if row.PUBLICROAD == "Yes":
        row.building_type_id = 12
    if (row.OWNERNAME == "BIBLICAL MINISTRIES WORLDWIDE")  or (row.OWNERNAME == "KRISHNA TEMPLE CORPORATION") or (row.OWNERNAME == "FELLOWSHIP BIBLE CHURCH") or (row.OWNERNAME == "FIRST BAPTIST CHURCH OF PLEASANT GROVE") or (row.OWNERNAME == "CATHOLIC DIOCESE OF SALT LAKE CITY REAL ESTATE CORPORATION") or (row.OWNERNAME == "CORP PRES BISHOP LDS CHURCH") or (row.OWNERNAME == "INTERNATIONAL FOURSQUARE GOSPEL CHURCH"):
        row.building_type_id = 10
            #All non-LDS Churches listed
    if (row.OWNERNAME == "CORP ") or (row.OWNERNAME == "PAYSON 1ST CORP L D S CHURCH") or (row.OWNERNAME == "CORP OF PRES BISHOP LDS CHURCH") or (row.OWNERNAME == "TEMPLE CORPORATION OF CHURCH OF JESUS CHRIST OF LDS") or (row.OWNERNAME == "NEBO STAKE OF CHURCH OF JESUS CHRIST OF LDS") or (row.OWNERNAME == "TEMPLE CORP OF THE CHURCH OF JESUS CHRIST OF LDS") or (row.OWNERNAME == "CORP OF PRES BISHIP CHURCH OF JESUS CHRIST OF LDS") or (row.OWNERNAME == "CORP PRES BISHOP LDS CHRUCH") or (row.OWNERNAME == "SPRINGVILLE 1ST CORP CHURCH JESUS CHRIST OF LDS") or (row.OWNERNAME == "SPANISH FORK 1ST CORP CHURCH OF JESUS CHRIST OF LDS") or (row.OWNERNAME == "SANTAQUIN 1ST WARD CORP CHURCH OF JESUS CHRIST LDS") or (row.OWNERNAME == "MAPLETON CORP OF CHURCH OF JESUS CHRIST OF LDS") or (row.OWNERNAME == "SPRINGVILLE 9TH WARD CHURCH OF JESUS CHRIST OF LDS") or (row.OWNERNAME == "SPRINGVILLE UTAH STAKE CHURCH OF JESUS CHRIST LDS") or (row.OWNERNAME == "CORP OF THE PRES BISHOP CHURCH OF JESUS CHRIST OF L D S") or (row.OWNERNAME == "TEMPLE CORP OF THE CHURCH OF JESUS CHRIST OF LDS (ET AL)") or (row.OWNERNAME == "MANILA CORP OF CHURCH OF JESUS CHRIST OF LDS") or (row.OWNERNAME == "CORP OF PRESIDING BISHOP OF CHURCH OF JESUS CHRIST OF LDS") or (row.OWNERNAME == "AMERICAN FORK 4TH WARD CORP CHURCH JESUS CHRIST LDS") or (row.OWNERNAME == "LEHI STAKE OF THE CHURCH OF JESUS CHRIST OF LDS") or (row.OWNERNAME == "LEHI STAKE CHURCH OF JESUS CHRIST OF LDS") or (row.OWNERNAME == "LEHI STAKE CHURCH OF JESUS CHRIST OF LDS")  or (row.OWNERNAME == "CORP OF PRES BISHOP CHURCH OF JESUS CHRIST OF L D S") or (row.OWNERNAME == "CORP PRES BISOP LDS CHURCH") or (row.OWNERNAME == "CORP OF PRES BISHOP CHURCH OF JESUS CHRIST OF LDS (ET AL)"):
        row.building_type_id = 10
            #All LDS Churches listed
    if (row.OWNERNAME == "BOARD OF EDUCATION ALPINE SCHOOL DISTRICT") or (row.OWNERNAME == "BOARD OF EDUCATION OF PROVO CITY SCHOOL DISTRICT")  or (row.OWNERNAME == "PROVO CITY SCHOOL DISTRICT BOARD OF EDUCATION") or (row.OWNERNAME == "MUNICIPAL BUILDING AUTHORITY OF PROVO CITY SCHOOL DISTRICT") or (row.OWNERNAME == "PROVO SCHOOL DISTRICT") or (row.OWNERNAME == "BOARD OF EDUCATION CITY OF PROVO") or (row.OWNERNAME == "BOARD OF EDUCATION OF PROVO CITY SCHOOL DISTRCIT") or (row.OWNERNAME == "BOARD OF EDUCATION OF THE NEBO SCHOOL DISTRICT (ET AL)") or (row.OWNERNAME == "ALPINE SCHOOL DISTRICT BOARD OF EDUCATION") or (row.OWNERNAME == "NEBO SCHOOL DISTRICT BOARD OF EDUCATION") or (row.OWNERNAME == "PROVO CITY SCHOOL DISTRICT") or (row.OWNERNAME == "ALPINE SCHOOL DISTRICT") or (row.OWNERNAME == "BOARD OF EDUCATION PROVO SCHOOL DISTRICT") or (row.OWNERNAME == "BOARD OF EDUCATION OF NEBO SCHOOL DISTRICT THE (ET AL)") or (row.OWNERNAME == "NEBO SCHOOL DISTRICT") or (row.OWNERNAME == "BOARD OF EDUCATION ALPINE SCHOOL DISTRICT (ET AL)") or (row.OWNERNAME == "UTAH VALLEY STATE COLLEGE") or (row.OWNERNAME == "BRIGHAM YOUNG UNIVERSITY") or (row.OWNERNAME == "ALPINE SCHOOL DISTRICT") or (row.OWNERNAME == "BOARD OF EDUCATION OF NEBO SCHOOL DISTRICT") or (row.OWNERNAME == "BOARD OF EDUCATION OF NEBO SCHOOL DISTRICT (ET AL)") or (row.OWNERNAME == "ALPINE SCHOOL DISTRICT") or (row.OWNERNAME == "BOARD OF EDUCATION OF ALPINE SCHOOL DISTRICT THE") or (row.OWNERNAME == "BRIGHAM YOUNG UNIVERSITY") or (row.OWNERNAME == "BOARD OF EDUCATION OF PROVO CITY") or (row.OWNERNAME == "UTAH VALLEY UNIVERSITY") or (row.OWNERNAME == "BOARD OF EDUCATION PROVO CITY") or (row.OWNERNAME == "BOARD OF EDUCATION OF PROVO CITY (ET AL)") or (row.OWNERNAME == "BOARD OF EDUCATION OF ALPINE SCHOOL DISTRICT"):
        row.building_type_id = 9
            #Public Schools & All Colleges and Universities here in Utah County
    if (row.OWNERNAME == "MOUNTAINVILLE ACADEMY") or (row.OWNERNAME == "WALDEN SCHOOL OF LIBERAL ARTS THE")  or (row.OWNERNAME == "LAKEVIEW ACADEMY OF SCIENCE ARTS AND TECHNOLOGY") or (row.OWNERNAME == "RONALD WILSON REAGAN ACADEMY") or (row.OWNERNAME == "RANCHES ACADEMY INCORPORATED THE") or (row.OWNERNAME == "SPECTRUM ACADEMY") or (row.OWNERNAME == "MERIT COLLEGE PREPARATORY ACADEMY") or (row.OWNERNAME == "C S LEWIS ACADEMY") or (row.OWNERNAME == "UTAH CHARTER ACADEMIES") or (row.OWNERNAME == "AMERICAN LEADERSHIP ACADEMY INC") or (row.OWNERNAME == "FREEDOM ACADEMY FOUNDATION THE (ET AL)") or (row.OWNERNAME == "ODYSSEY CHARTER SCHOOL INC") or (row.OWNERNAME == "LINCOLN ACADEMY INCORPORATED") or (row.OWNERNAME == "AMERICAN HERITAGE SCHOOLS INC")  or (row.OWNERNAME == "NOAH WEBSTER ACADEMY") or (row.OWNERNAME == "JOHN HANCOCK CHARTER SCHOOL") or (row.OWNERNAME == "TIMPANOGOS ACADEMY THE (ET AL)"):
        row.building_type_id = 9
            #Private & Charter Schools listed
    if row.OWNERNAME == "COMMON AREA":
        row.building_type_id = 12
    if row.OWNERNAME == "PACIFI CORP (ET AL)":
        row.building_type_id = 3
    if (row.OWNERNAME == "SPANISH FORK CITY") or (row.OWNERNAME == "UTAH DEPARTMENT OF TRANSPORTATION"):
        if row.TXACCTTYPE == "EXEMPT":
            row.building_type_id = 12
    if (row.OWNERNAME == "UTAH COUNTY"):
        row.building_type_id = 6
    if (row.OWNERNAME == "UNITED STATES POSTAL SERVICES") or (row.OWNERNAME == "UTAH STATE DEPT ADMIN SERVICES") or (row.OWNERNAME == "UTAH STATE ARMORY BOARD"):
        row.building_type_id = 8
    if (row.OWNERNAME == "TARGET CORPORATION") or (row.OWNERNAME == "UTAH STATE BUILDING OWNERSHIP AUTHORITY"):
            row.building_type_id = 4
    if (row.OWNERNAME == "UTAH STATE DEPT OF NATURAL RESOURCES") or (row.OWNERNAME == "UNITED STATES OF AMERICA") or (row.OWNERNAME == "UNITED STATES OF AMERICA (ET AL)") or (row.OWNERNAME == "UNITED STATES OF AMERICA THE"):
        row.building_type_id = 14
         # All non-arable land and mountains

    if row.USEDSCRP == "VACANT":
        if row.TXACCTTYPE == "RESIDENTIAL":
            if (row.CLASSDSCRP == "Vac Res Ac w/ Det Struct") or (row.CLASSDSCRP == "Vac Sub Lot w/ Det Struct") or (row.CLASSDSCRP == "Salvage Imp") or (row.CLASSDSCRP == "Vac Res Ac")  or (row.CLASSDSCRP == "Vac Sub Lot"):
                row.building_type_id = 14
      #All arable and developable lands.

                
    rows.updateRow(row)
del row, rows

print ("Run successful")


ExamplePython.py
Displaying ExamplePython.py.
