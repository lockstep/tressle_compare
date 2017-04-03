require 'rails_helper'

feature 'Search page' do
  context 'user is signed in' do
    before { @user = create(:user) }
    include_context 'signed in user'

    context 'products exist' do
      before do
        @desk = create(:product)
        @cabinet = create(:product, name: 'Red Cabinet', description: 'Nice cabinet')

        @amazon = create(:retailer)
        @ebay = create(:retailer, name: 'Ebay')

        create(:retailer_product, product: @desk, retailer: @amazon)
        create(:retailer_product, product: @desk, retailer: @ebay, current_price: 1000)
        create(:retailer_product, product: @cabinet, retailer: @amazon, current_price: 456.7)
      end

      scenario 'user sees products in list' do
        visit products_path
        expect(page).to have_content 'Study Desk'
        expect(page).to have_content 'Red Cabinet'
      end

      scenario 'user can sort products by name ascending' do
        visit products_path
        click_link_or_button 'Sort by'
        all('.sort-product .dropdown-item')[0].click
        within first('.product') do
          expect(page).to have_content 'Red Cabinet'
        end
      end

      scenario 'user can sort products by name descending' do
        visit products_path
        click_link_or_button 'Sort by'
        all('.sort-product .dropdown-item')[1].click
        within first('.product') do
          expect(page).to have_content 'Study Desk'
        end
      end

      scenario 'user can sort products by price ascending' do
        visit products_path
        click_link_or_button 'Sort by'
        all('.sort-product .dropdown-item')[2].click
        within first('.product') do
          expect(page).to have_content 'Study Desk'
          expect(page).to have_content '$123.45'
        end
      end

      scenario 'user can sort products by price descending' do
        visit products_path
        click_link_or_button 'Sort by'
        all('.sort-product .dropdown-item')[3].click
        within first('.product') do
          expect(page).to have_content 'Study Desk'
          expect(page).to have_content '$1,000.00'
        end
      end

      scenario 'user can search products', js: true do
        visit products_path
        complete_search_form
      end
    end
  end

  context 'user is not signed in' do
    scenario 'user is asked to log in' do
      visit products_path
      expect(page).to have_content 'Login'
    end
  end

  def complete_search_form(overrides={})
    within '#search-product-form' do
      fill_in 'query', with: overrides[:query] || 'desk'
      find('#query').native.send_keys(:return)
    end
  end
end
