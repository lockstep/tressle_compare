FactoryGirl.define do
  factory :product do
    name 'Study Desk'
    description 'Nice desk'
    code 'ABC123'
    width 10.2
    height 12.3
    depth 4.56
    color 'Black'
    material 'Wood'
    weight 123.45
    assembly_required true
    image_url 'http://example.com/test.png'
  end
end
