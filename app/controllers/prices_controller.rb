class PricesController < ApplicationController
  # before_action :authenticate_user!

  def index
    @price_list = Price.all.includes(:product, :retailer)
    @price_list = @price_list.search(params[:query]) if params[:query].present?
    sorting
    @price_list = @price_list.page(params[:page]).per(5)
  end

  private

  def sorting
    @sort = params[:sort] || 'price'
    @sort_direction = params[:sort_direction] || 'ASC'
    sort = (@sort == 'name') ? 'products.name' : @sort
    @price_list = @price_list.order("#{sort} #{@sort_direction}")
  end
end
