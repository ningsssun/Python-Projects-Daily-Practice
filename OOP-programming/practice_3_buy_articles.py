import pandas
from fpdf import FPDF

df = pandas.read_csv("articles.csv", dtype={"id": str})


class Article:
    def __init__(self, article_id):
        self.id = article_id
        self.name = df.loc[df["id"] == self.id, "name"].squeeze()
        self.price = df.loc[df["id"] == self.id, "price"].squeeze()

    def in_stock(self):
        in_stock = df.loc[df["id"] == self.id, "in stock"].squeeze()
        return in_stock


class InvoicePrintor:
    def __init__(self, article):
        self.article = article

    def print(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Receipt nr.{self.article.id}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Article: {self.article.name}", ln=1)

        pdf.set_font(family="Times", size=16, style="B")
        pdf.cell(w=50, h=8, txt=f"Price: {self.article.price}", ln=1)

        pdf.output("receipt.pdf")


print(df)
article_ID = input("Choose an article to buy: ")
article = Article(article_id=article_ID)
if article.in_stock():
    invoice = InvoicePrintor(article)
    invoice.print()
else:
    print("The article is not in stock")
