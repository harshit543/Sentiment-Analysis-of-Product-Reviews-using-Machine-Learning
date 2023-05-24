#importing .py libraries
import amz_comments_scraper
import ecom_prod_scraper
import ProductReviewAnalysis
import ProjectVisualisations

#Device specific headers at https://httpbin.org/get
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}

# exec_code(product, brand, time_limit, device_specific_headers)
df, brand_present_df = ecom_prod_scraper.exec_code("Infinix hot 10","",20,headers)

df = df.sort_values(by=['product_price'],ascending=False)
print(df.to_csv("teri maka bharosa.csv"))
print("Total number of products scrapped in 30 seconds are ", len(df),df.iloc[1].to_dict())