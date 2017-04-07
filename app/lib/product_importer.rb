module ProductImporter
  def self.import!
    scraping = Scrapinghub::Scrapinghub.new(ENV['SCRAPINGHUB_API_KEY'])
    project_id = ENV['SCRAPINGHUB_PROJECT_ID']
    scraping.spiders(project: project_id).response['spiders'].each do |spider|
      # NOTE: What does this protect us against?
      next if spider['version'].nil?

      items = scraping.spider_items(
        project: project_id,
        spider: spider['id']
      ).response
      save_or_update_products(items)
    end
  end

  def self.save_or_update_products(items)
    items.each do |item|
      next if item['url'].blank?
      product = Product.where(external_url: item['url'].split('?').first)
        .first_or_initialize
      product.update({
        name: extract_data(item['name']),
        manufacturer: extract_data(item['manufacturer']),
        manufacturer_sku: extract_data(item['manufacturer_sku']),
        description: extract_data(item['description']),
        sku: extract_data(item['sku']),
        image_url: extract_data(item['primary_image_url']),
        original_price: extract_data(item['original_price']),
        current_price: extract_data(item['current_price']),
        average_rating: extract_data(item['average_rating']),
        ratings_count: extract_data(item['ratings_count']),
        primary_category: extract_data(item['primary_category']),
        secondary_category: extract_data(item['secondary_category']),
        tertiary_category: extract_data(item['tertiary_category']),
        color: extract_data(item['color']),
        material: extract_data(item['material']),
      })
    end
  end

  def self.extract_data(result)
    if result && result.is_a?(Array)
      return result.first[1..-1] if result.first[0] == '$'
      return result.first
    else
      return result.scan(/SKU: (.*)/i).join if result =~ /SKU/i
      result
    end
  end
end
