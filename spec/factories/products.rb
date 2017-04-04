FactoryGirl.define do
  factory :product do
    name 'Study Desk'
    description 'Nice desk'
    manufacturer 'OMG Furnitures'
    sku 'ABC123'
    image_url 'http://example.com/test.png'
    external_url 'http://example.com/test'
    current_price 123.45
    primary_category 'Living'
    secondary_category 'Chairs & Desks'
  end

  factory :product_hello_doormat, parent: :product do
    name 'Hello Doormat'
    description 'Over-sized to provide more coverage, this beautiful doormat is made of natural coir, a durable, dense fiber that scrapes shoes clean.'
  end

  factory :product_biker_doormat, parent: :product do
    name 'Bear Biker Doormat'
    description 'Over-sized to provide more coverage, this beautiful doormat is made of natural coir, a durable, dense fiber that scrapes shoes clean.'
  end

  factory :product_bicycle_doormat, parent: :product do
    name 'Bicycle Doormat, Red and Black'
    description 'Premium 24-oz. anti-static polypropylene mat traps dirt, water and mud This commercial grade mat will not mold or rot & is highly resistant to extreme elements, including intense sunlight. Perfect for entry ways, garages, or any high traffic area in and around your home Molded design will not crush or break down over time or use.'
  end
end
