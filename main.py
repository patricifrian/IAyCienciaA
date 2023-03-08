#Author: Patricia Cifrián Pérez

from grobid_client_python.grobid_client.grobid_client import GrobidClient
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
import pathlib
import sys
import re



# Create client
grobid_client = GrobidClient("http://localhost:8070")

# Directory where the PDF files are stored
dirPdf = "./open-access-articles"
dirResults = "./results"
# Crear y abrir el fichero de salida  en modo de escritura
archivo = open(os.path.join(os.getcwd(), "results.txt"), "w")
nums = []

i = 1





# Get abstract information
def getAbstract(respuesta):
       abstract = texto[texto.find("<abstract>") + len("<abstract>"): texto.find("</abstract>")]
       return abstract

# Number of figure per article
def getNumFigures(respuesta):
       figures = len(re.findall(r"<figure(.*?)</figure>", respuesta, re.DOTALL))
       return figures

# List of links per article
def getLinks(respuesta):
       pattern = r'<ptr target="(https?://[^\s]+)"'
       linkList = re.findall(pattern, text)
       if len(linkList) == 0:
              archivo.write("No links in article\n")
       else:
              archivo.write("Found links:\n")
              for link in linkList:
                     archivo.write(link + "\n")

       archivo.write("\n")


# Create WordCloud
def getWordCloud(abstract):
       wordcloud = WordCloud(width=400, height=400, min_font_size=8).generate(abstract)

def plotWordCloud(wordcloud,pdf):
       plt.figure(figsize=(8, 8))
       plt.imshow(wordcloud)
       plt.axis("off")
       plt.show()
       imageName = "wordClouds/" + fichero.name + "_WordCloud.png"
       wordcloud.to_file(imageName)

def main():
       for fichero in dirPdf.iterdir():
              archivo.write(fichero.name + "\n")

              response = grobid_client.process_pdf("processFulltextDocument", str(fichero), generateIDs=False,
                                                   consolidate_header=False, consolidate_citations=False,
                                                   include_raw_citations=False, include_raw_affiliations=False,
                                                   tei_coordinates=False, segment_sentences=False)
              answer = str(response)
              # Check for correct answer
              if response[1]==200:
                     print("Codigo HTTP ",response[1])
                     abstract = getAbstract(answer)
                     wordcloud = getWordCloud(str(abstract))
                     plotWordCloud(wordcloud,fichero)
                     figures = getNumFigures(answer)
                     numFigures.append(figures)
                     links = getLinks(answer)
                     archivo.write("\n")

              else:
                     print("Codigo HTTP ", response[1])

              if response[1] == 200:
                     articles = ["Art1", "Art2", "Art3", "Art4", "Art5", "Art6", "Art7", "Art8", "Art9", "Art10"]
                     plt.bar(articles, figures)
                     plt.title("Number of figures per article")
                     plt.xlabel('Articles')
                     plt.ylabel('Number of figures')
                     plt.savefig("histogram_num_figures.jpg")


if __name__ == '__main__':
       main()