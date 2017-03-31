module ProductImporter
  def self.import!
    scraping = Scrapinghub::Scrapinghub.new(ENV['SCRAPINGHUB_API_KEY'])
    scraping.projects.response['projects'].each do |project_id|
      scraping.spiders(project: project_id).response['spiders'].each do |spider|
        retailer = Retailer.where(website: spider['id']).first_or_initialize
        retailer.update(name: spider['id'])
        next if spider['version'].nil?

        items = scraping.spider_items(
          project: project_id,
          spider: spider['id']
        ).response
        manipulate_product(items, retailer) if items.size > 0
      end
    end
  end

  def self.manipulate_product(items, retailer)
    items.each do |item|
      product_name = extract_data(item['name'])
      if product_name
        product = Product.where(name: product_name).first_or_initialize
        product.update({
          name: product_name,
          manufacturer: extract_data(item['manufacturer']),
          description: extract_data(item['description']),
          sku: extract_data(item['sku']),
          image_url: extract_data(item['primary_image_url'])
        })

        comparison = Comparison.where(
          product: product, retailer: retailer
        ).first_or_initialize
        comparison.update({
          original_price: extract_data(item['original_price']),
          current_price: extract_data(item['current_price']),
          average_rating: extract_data(item['average_rating']),
          ratings_count: extract_data(item['ratings_count']),
          url: extract_data(item['url'])
        })
      end
    end
  end

  def self.extract_data(result)
    if result && result.is_a?(Array)
      return result.first[1..-1] if result.first[0] == '$'
      return result.first
    else
      result
    end
  end
end
