FactoryGirl.define do
  factory :product do
    name 'Study Desk'
    description 'Nice desk'
    manufacturer 'OMG Furnitures'
    manufacturer_sku 'ABC123'
    image_url 'http://example.com/test.png'
    external_url 'http://example.com/test'
    current_price 123.45
    primary_category 'Living'
    secondary_category 'Chairs & Desks'
    retailer 'redhome'
  end
end
