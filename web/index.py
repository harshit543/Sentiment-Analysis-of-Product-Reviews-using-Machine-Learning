
import matplotlib.pyplot

matplotlib.pyplot.switch_backend('Agg')

from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__, static_folder='./templates/static')
arr_df =[]


@app.route('/', methods=['GET', 'POST'])
def home():
    return app.send_static_file("index.html")


@app.route('/analyse', methods=['POST'])
def sentimentAnalysis():
    name =  request.form.get('prod_name', "")
    brand=  request.form.get('brand_name', "")


    # importing .py libraries
    import amz_comments_scraper
    import ecom_prod_scraper
    import ProductReviewAnalysis
    import ProjectVisualisations

    # Device specific headers at https://httpbin.org/get
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"}



    # exec_code(product, brand, time_limit, device_specific_headers)
    df, brand_present_df = ecom_prod_scraper.exec_code(f"{name}", f"{brand}", 20, headers)

    df = df.sort_values(by=['product_price'], ascending=False)
    data = df.iloc[1].to_dict()
    print(data)

    return render_template("reviews_analysis.html",
                           prd=name,
                           prod_price=brand,
                           ecommerce_website=data["ecommerce_website"],
                           prod_rat=data["product_rating"],
                           prod_rat_count=data["rating_count"],
                           prod_url=data["product_url"],
                           prod_img=data["poduct_image_url"]
                           )





if __name__ == '__main__':
    app.run(use_reloader=False, port=8001)
