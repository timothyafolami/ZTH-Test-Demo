import pandas as pd

# Define the list of names and surnames
names = [
    "Promise", "Elochukwu", "Ogechi", "Salawu", "Marie", 
    "Muriel", "Praise", "Ruth", "Tunde", "Udi", 
    "Mohammed", "Aleshinloye", "Godson", "Kenne", "Lucky", 
    "Linda", "Promise", "Chinwe", "Rebecca", "Emeti", 
    "Chidinma", "Ogbuade", "Olabisi", "Orji", "Promise", 
    "Hassan", "Aijoba", "Hamiel", "Ibukunoluwa", "Tobechukwu", 
    "Keren", "Adaeze", "Opene-Terry", "Mazi", "Daniella", 
    "Jennifer", "Olawuwo"
]

surnames = [
    "Arowosafe", "Onyinye", "Juliet", "Biliaminu Biola", "Laguerre", 
    "Tema", "Obuma", "Omoizirein", "Ogunsakin", "Blessing", 
    "Sajid", "Wasilat", "Nwaubani", "Nzoyim Martinien", "Okuna", 
    "Awotwe", "Ekele", "Ibemesi", "Ogu", "Vicent", 
    "Umennadi", "Tijani", "Oseni", "Patricia", "Taiwo", 
    "Nurudeen", "Ruth", "Olamide", "Deji", "Romanus", 
    "Happaneh", "Athanasius", "Josephine", "Charles", "Gumba", 
    "Coffie", "Toheeb"
]

# Create a DataFrame
df = pd.DataFrame({
    'First Name': names,
    'Last Name': surnames
})

# Display the DataFrame
# save to a csv file
df.to_csv('User_data.csv')
