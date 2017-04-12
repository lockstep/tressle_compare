Rails.application.routes.draw do
  namespace :admin do
    resources :products
    resources :users
    root to: "products#index"
  end

  devise_for :users
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  resources :products
  get 'categories', to: 'categories#index'

  root to: 'home#index'
end
