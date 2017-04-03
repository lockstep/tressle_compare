require 'rails_helper'

feature 'Product page' do
  context 'product exists' do
    before do
      @product = create(:retailer_product, current_price: 1000)
    end
    scenario "user can navigate to a retailer's product site" do
      visit root_path
      expect(page).to have_content 'Study Desk'
      click_on 'Study Desk'
      expect(page).to have_link('$1,000.00', href: @product.url)
    end
  end
end
