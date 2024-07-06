#Reportlab is a Python library that create documents 
#import necessary functions from the library
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

#add Serial number, Date , Item name , Item Price to create a bill or receipt
Items = [
    [ "S.no.", "Date" , "Item name", "Price (in Rs.)" ],
    ["1","11/04/2004","T-Shirt","450.00/-"],
    [ "2", "11/04/2004", "Shirt", "600.00/-"],
    [ "3", "11/04/2024", "Top","550.00/-"],
    [ "4", "11/04/2024", "Trouser","1050.00/-"],
    ["5", "11/04/2024", "Lower","450.00/-"],
    [ "6","11/04/2024", "Shorts","300.00/-"],
    [ "7","11/04/2024", "Jeans","1150.00/-"],
    [ "8","11/04/2024", "Jacket","950.00/-"],
    [ "Sub Total", "","","5550.00/-"],
    [ "Discount", "","","-150.00/-"],
    [ "Total", "","","5400.00/-"],
]

#we can add colors,styles,table etc. from this library
#define pdf function and styles
bill = SimpleDocTemplate( "PaymentReceipt.pdf" , pagesize = A4 )
styles = getSampleStyleSheet()
title_style = styles[ "Heading1" ]

title_style.alignment = 1

#the title of Payment Receipt
title = Paragraph( "Fashion Market" , title_style ) 

#Table of Bill
style = TableStyle(
    [
        ( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ),
        ( "GRID" , ( 0, 0 ), ( 8 , 8 ), 1 , colors.black ),
        ( "BACKGROUND" , ( 0, 0 ), ( 4, 0 ), colors.blueviolet),
        ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.white ),
        ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ),
        ( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.white ),
    ]
)

table = Table( Items, style = style )
#A Payment Receipt is created.
bill.build([ title , table ]) 

print("\nCheck your Folder, Receipt is Generated . \n Thank You !!!\n")