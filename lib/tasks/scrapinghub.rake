namespace :scrapinghub do
  desc "Importing data from Scrapinghub"
  task import: :environment do
    ProductImporter.import!
  end
end
