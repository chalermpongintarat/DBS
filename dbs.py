from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

with open("drug_list.txt", "r") as file: 
    line = file.read().split("\n")

    drug_bank_info_for = []
    
    for drug_id in line:

        url = "https://go.drugbank.com/drugs/"+drug_id

        response = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        url_open = urlopen(response).read()
        html_page = url_open.decode('utf-8')

        soup = BeautifulSoup(html_page, 'html.parser')
        soup.prettify()

        ##### DrugBank info #####
        col_xl_10_col_md_9_col_sm_8 = soup.find_all('dd', attrs={'class':'col-xl-10 col-md-9 col-sm-8'})
        drug_bank_info = []
        for p in col_xl_10_col_md_9_col_sm_8:
            info = p.find_all('p')
            drug_bank_info.append(info)

        i = drug_bank_info[0][0]
        if len(i):
            drug_bank_info_for.append(i)
        else:
            drug_bank_info_for.append("_blank_")
        # drug_bank_info_for.append(i)

    ##### DrugBank info #####
    f = open("drug_bank_info_for_000_200.txt", "w")
    for line in drug_bank_info_for:
        f.write(str(line))
        f.write("\n")
    f.close()
