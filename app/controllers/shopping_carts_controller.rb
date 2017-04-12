class ShoppingCartsController < ApplicationController
  def index
    @products = Product.where.not(image_url: nil, ratings_count: nil)
      .order('RANDOM()').limit(10)
  end
  def order_confirmation
  end
end
