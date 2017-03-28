require 'rails_helper'

feature 'Price List' do
  context 'user is signed in' do
    before { @user = create(:user) }
    include_context 'signed in user'

    context 'products exist' do
      before do
        @desk = create(:product)
        @cabinet = create(:product, name: 'Red Cabinet', description: 'Nice cabinet')

        @amazon = create(:retailer)
        @pronto = create(:retailer, name: 'Pronto')

        create(:price, product: @desk, retailer: @amazon)
        create(:price, product: @desk, retailer: @pronto, price: 1000)
        create(:price, product: @cabinet, retailer: @amazon, price: 456.7)
      end

      scenario 'user sees products with prices in list' do
        visit prices_path
        expect(page).to have_content 'Study Desk'
        expect(page).to have_content 'Red Cabinet'
        expect(page).to have_content '$123.45'
        expect(page).to have_content '$1,000.00'
        expect(page).to have_content '$456.70'
        product_rows = all('.product')
        expect(product_rows.size).to eq 3
      end

      scenario 'user can sort products by name ascending' do
        visit prices_path
        click_link_or_button 'Sort by'
        all('.sort-product .dropdown-item')[0].click
        within first('.product') do
          expect(page).to have_content 'Red Cabinet'
        end
      end

      scenario 'user can sort products by name descending' do
        visit prices_path
        click_link_or_button 'Sort by'
        all('.sort-product .dropdown-item')[1].click
        within first('.product') do
          expect(page).to have_content 'Study Desk'
          expect(page).to have_content '$123.45'
        end
      end

      scenario 'user can sort products by price ascending' do
        visit prices_path
        click_link_or_button 'Sort by'
        all('.sort-product .dropdown-item')[2].click
        within first('.product') do
          expect(page).to have_content 'Study Desk'
          expect(page).to have_content '$123.45'
        end
      end

      scenario 'user can sort products by price descending' do
        visit prices_path
        click_link_or_button 'Sort by'
        all('.sort-product .dropdown-item')[3].click
        within first('.product') do
          expect(page).to have_content 'Study Desk'
          expect(page).to have_content '$1,000.00'
        end
      end

      scenario 'user can search products', js: true do
        visit prices_path
        complete_search_form
        expect(page).to have_content 'Study Desk'
        expect(page).not_to have_content 'Red Cabinet'
        product_rows = all('.product')
        expect(product_rows.size).to eq 2
      end
    end
  end

  xcontext 'user is not signed in' do
    scenario 'user is asked to log in' do
      visit prices_path
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
