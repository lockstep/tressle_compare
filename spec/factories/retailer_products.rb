FactoryGirl.define do
  factory :retailer_product do
    product { create(:product) }
    retailer { create(:retailer) }
    original_price 200.5
    current_price 123.45
    average_rating 4.5
    ratings_count 56
    url 'www.example.com'
  end
end
