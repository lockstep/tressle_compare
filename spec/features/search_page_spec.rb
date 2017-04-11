require 'rails_helper'

feature 'Search page' do
  context 'user is signed in' do
    before { @user = create(:user) }
    include_context 'signed in user'

    context 'products exist' do
      before do
        @desk = create(:product)
        @cabinet = create(:product,
          name: 'Red Cabinet',
          description: 'Nice cabinet',
          current_price: 1000
        )
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
          expect(page).to have_content 'Red Cabinet'
          expect(page).to have_content '$1,000.00'
        end
      end
    end
  end

  context 'user is not signed in' do
    scenario 'user is asked to log in' do
      visit products_path
      expect(page).to have_content 'Login'
    end
  end
end
