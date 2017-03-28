require 'rails_helper'

feature 'Product' do
  context 'products exist' do
    before do
      @desk = create(:product)

      @amazon = create(:retailer)
      @pronto = create(:retailer, name: 'Pronto')

      create(:price, product: @desk, retailer: @amazon)
      create(:price, product: @desk, retailer: @pronto, price: 456.78)
    end

    scenario 'user sees product detail' do
      visit product_path(@desk)
      expect(page).to have_content @desk.name
      expect(page).to have_content @desk.description
    end

    scenario 'user sees price comparison of product' do
      visit product_path(@desk)
      within first('table#price-comparison tr.price') do
        expect(page).to have_content @amazon.name
        expect(page).to have_content '$123.45'
        expect(page).to have_content 'Best Price'
      end
      within all('table#price-comparison tr.price')[1] do
        expect(page).to have_content @pronto.name
        expect(page).to have_content '$456.78'
        expect(page).not_to have_content 'Best Price'
      end
    end
  end
end
