from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker

# 生成城市地图
c1 = (
    Map(init_opts=opts.InitOpts(width="1920px", height="1080px"))
    .add(
        "我的足迹",
        [
            # 直辖市
            ["北京", 22], ["天津", 20], ["重庆", 23], ["上海", 19],
            # 山东省
            ["潍坊", 23], ["日照", 23], ["济南", 17], ["青岛", 16], ["烟台", 10], ["威海", 12], ["泰安", 11], ["临沂", 8],
            # 内蒙古
            ["锡林郭勒盟", 18], ["乌兰察布", 18],
            # 陕西
            ["西安", 11],
            # 山西
            ["大同", 22],
            # 辽宁
            ["大连", 12],
            # 江苏
            ["南京", 20], ["苏州", 13], ["扬州", 13], ["无锡", 13], ["南通", 13],
            # 浙江
            ["杭州", 22], ["嘉兴", 22],
            # 湖南
            ["长沙", 20], ["张家界", 20], ["湘西", 20],
            # 四川
            ["成都", 23],
            # 广东
            ["广州", 15], ["深圳", 15], ["珠海", 15],
        ],
        "china-cities",
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-中国地图（带城市）"),
        visualmap_opts=opts.VisualMapOpts(),
    )
    .render("map_china_cities.html")
)

# 生成省份地图
c2 = (
    Map(init_opts=opts.InitOpts(width="1920px", height="1080px"))
    .add(
        "我的足迹",
        [
            # 直辖市
            ["北京", 22], ["天津", 19], ["重庆", 23], ["上海", 19],
            ["山东", 23], ["内蒙古", 18], ["陕西", 11], ["山西", 22], ["辽宁", 12], ["江苏", 20], ["浙江", 22],["湖南", 20],
            ["四川", 23], ["广东", 15],
        ],
        "china",
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Map-中国地图"),
        visualmap_opts=opts.VisualMapOpts(),
    )
    .render("map_china.html")
)