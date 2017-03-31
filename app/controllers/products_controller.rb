class ProductsController < ApplicationController
  # before_action :authenticate_user!

  def index
    @products = Product.with_comparisons
    @products = @products.search(params[:query]) if params[:query].present?
    sort_products
    @products = @products.page(params[:page]).per(5)
  end

  def show
    @product = Product.find(params[:id])
  end

  private

  def sort_products
    @sort = params[:sort] || 'name'
    @sort_direction = params[:sort_direction] || 'ASC'
    sort = (@sort == 'price') ? 'comparisons.current_price' : @sort
    @products = @products.order("#{sort} #{@sort_direction} NULLS LAST")
  end
end
