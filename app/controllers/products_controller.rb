class ProductsController < ApplicationController
  # before_action :authenticate_user!

  def index
    @products = Product.all
    @products = @products.search(params[:query]) if params[:query].present?
    if params[:secondary_category].present?
      @products = @products.where(secondary_category: params[:secondary_category])
    end
    sort_products
    @products = @products.page(params[:page]).per(12)
  end

  def show
    @product = Product.find(params[:id])
  end

  private

  def sort_products
    @sort = params[:sort] || 'name'
    @sort_direction = params[:sort_direction] || 'ASC'
    @products = @products.order("#{@sort} #{@sort_direction} NULLS LAST")
  end
end
