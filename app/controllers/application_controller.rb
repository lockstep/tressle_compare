class ApplicationController < ActionController::Base
  if Rails.env.production?
    http_basic_authenticate_with name: "tressle", password: "T2017"
  end
  protect_from_forgery with: :exception
end
