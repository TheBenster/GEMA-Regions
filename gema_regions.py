import csv

gema_regions = {
    1: ["Union", "Towns", "Rabun", "Lumpkin", "White", "Habersham", "Stephens", "Hall", "Banks", "Franklin",
        "Hart", "Jackson", "Madison", "Elbert", "Barrow", "Oconee", "Clarke", "Elbert", "Oglethrope", "Wilkes", "Lincoln", "Wilkes",
        "Greene", "Morgan", "Walton", "Newton"],
    2: ["Crisp", "Quitman", "Randolph", "Terrell", "Lee", "Turner", "Worth", "Tift", "Dougherty", "Calhoun",
        "Clay", "Early", "Baker", "Miller", "Mitchell", "Colquitt", "Cook", "Seminole", "Decatur", "Grady", "Thomas",
        "Brooks", "Lowndes"],
    3: ["Jasper", "Putnam", "Taliaferro", "Hancock", "Warren", "McDuffle", "Columbia", "Glascock", "Richmond", 
        "Baldwin", "Washington", "Jefferson", "Burke", "Twiggs", "Wilkinson", "Johnson", "Laurens", "Treutlen",
        "Emanuel", "Candler", "Jenkins", "Bulloch", "Screven"],
    4: ["Troup", "Meriwether", "Pike", "Spalding", "Butts", "Lamar", "Monroe", "Upson", "Jones", "Bibb", "Talbot", "Harris",
        "Muscogee", "Taylor", "Crawford", "Peach", "Houston", "Macon", "Dooly", "Schley", "Marion", "Chattahoochee",
        "Stewart", "Webster", "Sumter"],
    5: ["Charlton", "Camden", "Brantley", "Pierce", "Wayne", "McIntosh", "Glynn", "Long", "Liberty", "Bryan",
        "Chatham", "Effingham"],
    6: ["Dade", "Catoosa", "Whitfield", "Murray", "Fannin", "Walker", "Chattooga", "Gordon", "Gilmer", "Pickens",
        "Floyd", "Dawson", "Cherokee", "Forsyth", "Bartow", "Polk", "Paulding", "Haralson", "Carroll", "Heard", "Coweta"],
    7: ["Cobb", "Gwinnett", "Fulton", "Douglass", "DeKalb", "Rockdale", "Clayton", "Henry", "Fayette"],
    8: ["Bleckley", "Pulaski", "Dodge", "Wilcox", "Telfair", "Montgomery", "Wheeler", "Toombs", "Tattnall", 
        "Appling", "Jeff Davis", "Coffee", "Bacon", "Ware", "Clinch", "Echols", "Lanier", "Atkinson", "Berrien", "Irwin", 
        "Ben Hill",]
}


with open("gema_regions.csv", 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['County', 'Region'])
    
    for region_num, counties in gema_regions.items():
        for county in counties:
            w.writerow([county, region_num])