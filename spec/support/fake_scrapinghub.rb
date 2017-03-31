require 'sinatra/base'

class FakeScrapinghub < Sinatra::Base
  get '/api/scrapyd/listprojects.json' do
    json_response 200, 'projects.json'
  end

  get '/api/spiders/list.json' do
    json_response 200, 'spiders.json'
  end

  get '/api/items.json' do
    if params[:spider] =~ /example2/
      json_response 200, 'items2.json'
    else
      json_response 200, 'items.json'
    end
  end

  def json_response(response_code, file_name)
    content_type :json
    status response_code
    File.open(Rails.root.join('spec', 'fixtures', 'scrapinghub', file_name), 'rb')
  end
end
