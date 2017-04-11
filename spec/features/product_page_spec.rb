require 'rails_helper'

feature 'Product page' do
  context 'product exists' do
    before { @product = create(:product) }

    scenario "user sees product detail" do
      visit products_path
      expect(page).to have_content 'Study Desk'
      click_on 'Study Desk'
      expect(page).to have_content @product.description
    end

    scenario "user can navigate to a retailer's product site" do
      visit products_path
      expect(page).to have_content 'Study Desk'
      click_on 'Study Desk'
      expect(page).to have_link('BUY', href: @product.external_url)
    end
  end
end
