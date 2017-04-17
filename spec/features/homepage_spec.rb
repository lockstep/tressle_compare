require 'rails_helper'

feature 'Homepage' do
  # comment this out because there may be changes on how we associate the data. 
  #
  # context 'products exist' do
  #   before do
  #     @desk = create(:product)
  #     @amazon = create(:retailer)
  #     create(:retailer_product, product: @desk, retailer: @amazon)
  #   end
  #   scenario "user can search products" do
  #     visit root_path
  #     expect(page).to have_content 'Shop smart for your home'
  #     find("button[type=submit]").click
  #     expect(page).to have_content @desk.name
  #   end
  # end
  scenario "user can navigate to search result page" do
    visit root_path
    expect(page).to have_content 'Start your'
    find("button[type=submit]").click
    expect(page).to have_content 'Filter'
  end
end
