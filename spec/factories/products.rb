FactoryGirl.define do
  factory :product do
    name 'Study Desk'
    description 'Nice desk'
    manufacturer 'OMG Furnitures'
    sku 'ABC123'
    image_url 'http://example.com/test.png'
    external_url 'http://example.com/test'
    current_price 2.3
  end
end
