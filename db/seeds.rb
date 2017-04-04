# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)

product1 = Product.where(name: 'Hello Doormat from Houzz').first_or_create do |product|
  product.description = 'Over-sized to provide more coverage, this beautiful doormat is made of natural coir, a durable, dense fiber that scrapes shoes clean.'
  product.sku = '1234'
  product.image_url = 'https://st.hzcdn.com/simgs/4391ae6807802694_4-5659/contemporary-doormats.jpg'
  product.external_url = 'http://www.houzz.com/test/product/1234'
  product.current_price = 100
end

product1_1 = Product.where(name: 'Hello Doormat from Wayfair').first_or_create do |product|
  product.description = 'Over-sized to provide more coverage, this beautiful doormat is made of natural coir, a durable, dense fiber that scrapes shoes clean.'
  product.sku = '1234'
  product.image_url = 'https://st.hzcdn.com/simgs/4391ae6807802694_4-5659/contemporary-doormats.jpg'
  product.external_url = 'http://www.wayfair.com/test/product/1234'
  product.current_price = 120
end

product2 = Product.where(name: 'Bear Biker Doormat from Hayneedle').first_or_create do |product|
  product.description = 'Over-sized to provide more coverage, this beautiful doormat is made of natural coir, a durable, dense fiber that scrapes shoes clean.'
  product.sku = '1235'
  product.image_url = 'https://st.hzcdn.com/simgs/dc1164d9078025ae_4-5441/eclectic-doormats.jpg'
  product.external_url = 'https://www.hayneedle.com/photos/product/1235'
  product.current_price = 60
end

product2_1 = Product.where(name: 'Bear Biker Doormat from Wayfair').first_or_create do |product|
  product.description = 'Over-sized to provide more coverage, this beautiful doormat is made of natural coir, a durable, dense fiber that scrapes shoes clean.'
  product.sku = '1235'
  product.image_url = 'https://st.hzcdn.com/simgs/dc1164d9078025ae_4-5441/eclectic-doormats.jpg'
  product.external_url = 'https://www.wayfair.com/photos/product/1235'
  product.current_price = 65
end

product3 = Product.where(name: 'Bicycle Doormat, Red and Black').first_or_create do |product|
  product.description = 'Premium 24-oz. anti-static polypropylene mat traps dirt, water and mud This commercial grade mat will not mold or rot & is highly resistant to extreme elements, including intense sunlight. Perfect for entry ways, garages, or any high traffic area in and around your home Molded design will not crush or break down over time or use.'
  product.sku = '1236'
  product.image_url = 'https://st.hzcdn.com/simgs/99617e570429955d_4-4966/contemporary-doormats.jpg'
  product.external_url = 'https://www.houzz.com/test/1236'
  product.current_price = 90
end

