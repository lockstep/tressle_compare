FactoryGirl.define do
  factory :user do
    sequence(:email) {|n| "person#{n}@example.com"}
    password '1234test'
  end
end
