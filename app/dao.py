def load_catgories():
    return [{
        "id": 1,
        "name": "Mobile"
    }, {
        "id": 2,
        "name": "Tablet"
    }]


def load_products(kw):
    product= [{
        "id": 1,
        "name": "Ipad pro 2023",
        "price": 200000,
        "image": "https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/refurb-ipad-pro-12-wifi-spacegray-2019?wid=1144&hei=1144&fmt=jpeg&qlt=80&op_usm=0.5,0.5&.v=1563570657454"
    }, {
        "id": 2,
        "name": "Iphone 15",
        "price": 205000,
        "image": "https://mobilepriceall.com/wp-content/uploads/2022/09/Apple-iPhone-14-1024x1024.jpg"
    }, {
        "id": 3,
        "name": "Iphone 14",
        "price": 155000,
        "image": "https://m.xcite.com/media/catalog/product//i/p/iphone_14_pro_-_silver_1_1_1.jpg"
    }, {
        "id": 4,
        "name": "Iphone 13",
        "price": 105000,
        "image": "https://www.dslr-zone.com/wp-content/uploads/2021/10/3-2-768x768.jpeg"
    }, {
        "id": 5,
        "name": "Iphone 12",
        "price": 55000,
        "image": "https://th.bing.com/th/id/OIP.Xfo1aHIjLGIizcUPueZDWAHaIF?pid=ImgDet&rs=1"
    }]

    if kw:
        product=[p for p in product if p['name'].find(kw)>=0]
    return product
