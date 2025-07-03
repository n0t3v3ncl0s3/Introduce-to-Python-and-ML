import pandas as pd

# 1. Đọc dữ liệu từ file CSV
# TODO: Đọc file 'sales_data.csv' vào một DataFrame tên là df
df = pd.read_csv("data_processed.csv")

# 2. Thêm cột 'Revenue' = Quantity * Price
# TODO: Tạo cột mới 'Revenue' trong df
df['Revenue'] = df['Quantity']*df['Price']

# 3. Tính tổng doanh thu theo ngày
# TODO: Nhóm theo 'Date' và tính tổng 'Revenue'
daily_revenue = df.groupby("Date")["Revenue"].sum()
print("Tổng doanh thu theo ngày:")
print(daily_revenue)

# 4. Tính tổng doanh thu theo sản phẩm
# TODO: Nhóm theo 'Product' và tính tổng 'Revenue'
product_revenue = df.groupby("Product")["Revenue"].sum()
print("\nTổng doanh thu theo sản phẩm:")
print(product_revenue)

# 5. Tìm sản phẩm có doanh thu cao nhất
# TODO: Tìm tên sản phẩm có doanh thu lớn nhất
top_product = product_revenue.idxmax()
print(f"\nSản phẩm có doanh thu cao nhất: {top_product}")