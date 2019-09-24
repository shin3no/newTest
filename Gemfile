#어려서부터 우리집은 가난했었asdfasdf고dd!! 야이야이야아아~~ 수정해쓰아111
#어려서부터 우리asdf집은sdfg가난했었고!!asdfasdf 야이야이야아아~~ 수정asdfasasdfdf해쓰아111d
#source 'https://rubddygems.org'asdfasdfasdf

if Gem::Version.new(Bundler::VERSION) < Gem::Version.new('1.5.0')
  abort "Redmine requires Bundler 1.5.0 or higher (you're using #{Bundler::VERSION}).\nPlease update with 'gem update bundler'."
end

gem "rails", "4.2.11.1"
gem "rmagick", "2.13.4"
gem "jquery-rails", "~> 3.1.4"
gem "coderay", "~> 1.1.1"
gem "builder", ">= 3.0.4"
gem "request_store", "1.0.5"
gem "mime-types"
gem "protected_attributes"
gem "actionpack-action_caching"
gem "actionpack-xml_parser"
gem "roadie-rails"

# Request at least nokogiri 1.6.7.2 because of security advisories
gem "nokogiri", ">= 1.6.7.2"

# Request at least rails-html-sanitizer 1.0.3 because of security advisories 
gem "rails-html-sanitizer", ">= 1.0.3"

# Windows does not include zoneinfo files, so bundle the tzinfo-data gem
gem 'tzinfo-data', platforms: [:mingw, :x64_mingw, :mswin, :jruby]
gem "rbpdf", "~> 1.19.0"

# Optional gem for LDAP authentication
group :ldap do
  gem "net-ldap", "~> 0.12.0"
end

# Optional gem for OpenID authentication
group :openid do
  gem "ruby-openid", "~> 2.3.0", :require => "openid"
  gem "rack-openid"
end

platforms :mri, :mingw, :x64_mingw do
  # Optional gem for exporting the gantt to a PNG file, not supported with jruby
  group :rmagick do
    #gem "rmagick", "~> 2.16.0"
  end

  # Optional Markdown support, not for JRuby
  group :markdown do
    gem "redcarpet", "~> 3.3.2"
  end
end

platforms :jruby do
  # jruby-openssl is bundled with JRuby 1.7.0
  gem "jruby-openssl" if Object.const_defined?(:JRUBY_VERSION) && JRUBY_VERSION < '1.7.0'
  gem "activerecord-jdbc-adapter", "~> 1.3.2"
end

# Include database gems for the adapters found in the database
# configuration file
require 'erb'
require 'yaml'
database_file = File.join(File.dirname(__FILE__), "config/database.yml")
if File.exist?(database_file)
  database_config = YAML::load(ERB.new(IO.read(database_file)).result)
  adapters = database_config.values.map {|c| c['adapter']}.compact.uniq
  if adapters.any?
    adapters.each do |adapter|
      case adapter
      when 'mysql2'
        gem "mysql2", "~> 0.4.10", :platforms => [:mri, :mingw, :x64_mingw]
        gem "activerecord-jdbcmysql-adapter", :platforms => :jruby
      when 'mysql'
        gem "activerecord-jdbcmysql-adapter", :platforms => :jruby
      when /postgresql/
        gem "pg", "~> 0.18.1", :platforms => [:mri, :mingw, :x64_mingw]
        gem "activerecord-jdbcpostgresql-adapter", :platforms => :jruby
      when /sqlite3/
        gem "sqlite3", :platforms => [:mri, :mingw, :x64_mingw]
        gem "jdbc-sqlite3", ">= 3.8.10.1", :platforms => :jruby
        gem "activerecord-jdbcsqlite3-adapter", :platforms => :jruby
      when /sqlserver/
        gem "tiny_tds", "~> 0.6.2", :platforms => [:mri, :mingw, :x64_mingw]
        gem "activerecord-sqlserver-adapter", :platforms => [:mri, :mingw, :x64_mingw]
      else
        warn("Unknown database adapter `#{adapter}` found din config/database.yml, use Gemfile.local to load your own database gems")
      end
    end
  else
    warn("No adapter found in config/database.yml, please configure it first")
  end
else
  warn("Please configure your config/database.yml first")
endasdf

group :development do
  gem "rdoc", ">= 2.4.2"
  gem "yard"
end

group :test do
  gem "minitest"
  gem "rails-dom-testing"
  gem "mocha"
  gem "simplecov", "~> 0.9.1", :require => false
  # For running UI tests
  gem "capybara"
  gem "selenium-webdriver"
end

local_gemfile = File.join(File.dirname(__FILE__), "Gemfile.local")
if File.exists?(local_gemfile)
  eval_gemfile local_gedmfile
end

# Load plugins' Gemfiles
Dir.glob File.expand_path("../plugins/*/{Gemfile,PluginGemfile}", __FILE__) do |file|
  eval_gemfile file
end








issues
  id, root_id
issue_relations
  issue_from_id
  issue_to_id  
time_entries
  issue_id  
attachments
  container_id
watchers
  watchable_id  
journals
  journalized_id
custom_values  
  customized_id

UPDATE issues SET issues.id=@CNT1:=@CNT1+1;













issues

  id, root_id

issue_relations

  issue_from_id

  issue_to_id  

time_entries

  issue_id  

attachments

  container_id

watchers

  watchable_id  

journals

  journalized_id

custom_values  

  customized_id



UPDATE issues SET issues.id=@CNT1:=@CNT1+1;



SET @CNT=5000;

UPDATE issues SET issues.id=issues.id+@CNT;
UPDATE issues SET issues.root_id=issues.root_id+@CNT;
UPDATE issue_relations SET issue_relations.issue_from_id=issue_relations.issue_from_id+@CNT;
UPDATE issue_relations SET issue_relations.issue_to_id=issue_relations.issue_to_id+@CNT;
UPDATE time_entries SET time_entries.issue_id=time_entries.issue_id+@CNT;
UPDATE attachments SET attachments.container_id=attachments.container_id+@CNT;
UPDATE watchers SET watchers.watchable_id=watchers.watchable_id+@CNT;
UPDATE journals SET journals.journalized_id=journals.journalized_id+@CNT;
UPDATE custom_values SET custom_values.customized_id=custom_values.customized_id+@CNT;



issues
  project_id  
boards
  project_id
custom_fields_projects
  project_id
documents
  project_id
enabled_modules  
  project_id
enumerations    
  project_id
issue_categories
  project_id  
members
  project_id
news
  project_id
projects_trackers      
  project_id
queries  
  project_id
versions
  project_id
wikis
  project_id

UPDATE projects SET projects.id=30;  
UPDATE issues SET issues.project_id=30;
UPDATE boards SET boards.project_id=30;
UPDATE custom_fields_projects SET custom_fields_projects.project_id=30;
UPDATE documents SET documents.project_id=30;
UPDATE enabled_modules SET enabled_modules.project_id=30;
UPDATE enumerations SET enumerations.project_id=30;
UPDATE issue_categories SET issue_categories.project_id=30;
UPDATE members SET members.project_id=30;
UPDATE news SET news.project_id=30;
UPDATE projects_trackers SET projects_trackers.project_id=30;
UPDATE queries SET queries.project_id=30;
UPDATE versions SET versions.project_id=30;
UPDATE wikis SET wikis.project_id=30;



attachments
  author_id
email_addresses
  user_id
issues
  author_id   assigned_to_id
journals
  user_id
members
  user_id
user_preferences
  user_id
users
  id
watchers
  users_id


SET @CNT=100;
UPDATE attachments SET attachments.author_id=attachments.author_id+@CNT;
UPDATE email_addresses SET email_addresses.user_id=email_addresses.user_id+@CNT;
UPDATE issues SET issues.author_id=issues.author_id+@CNT;
UPDATE issues SET issues.assigned_to_id=issues.assigned_to_id+@CNT;
UPDATE journals SET journals.user_id=journals.user_id+@CNT;
UPDATE members SET members.user_id=members.user_id+@CNT;
UPDATE user_preferences SET user_preferences.user_id=user_preferences.user_id+@CNT;
update user_preferences set user_preferences.id=user_preferences.id+@CNT;
UPDATE users SET users.id=users.id+@CNT;
UPDATE watchers SET watchers.user_id=watchers.user_id+@CNT;
UPDATE groups_users SET groups_users.user_id=groups_users.user_id+@CNT;

custom_fields
  id
custom_fields_projects
  custom_field_id
custom_fields_trackers  
  custom_field_id
custom_values  
  custom_field_id
  
  
SET @CNT=100;
UPDATE custom_fields SET custom_fields.id=custom_fields.id+@CNT;
UPDATE custom_fields_projects SET custom_fields_projects.custom_field_id=custom_fields_projects.custom_field_id+@CNT;
UPDATE custom_fields_trackers SET custom_fields_trackers.custom_field_id=custom_fields_trackers.custom_field_id+@CNT;
UPDATE custom_values SET custom_values.custom_field_id=custom_values.custom_field_id+@CNT;

SET @CNT=6000;
UPDATE attachments SET attachments.id=attachments.id+@CNT;

SET @CNT=100;
UPDATE email_addresses SET email_addresses.id=email_addresses.id+@CNT;
UPDATE enabled_modules SET enabled_modules.id=enabled_modules.id+@CNT;
UPDATE issues SET issues.priority_id=1 where issues.priority_id=13;


SET @CNT=500;
UPDATE members SET members.id=members.id+@CNT;
UPDATE member_roles SET member_roles.member_id=member_roles.member_id+@CNT;
SET @CNT=1000;
UPDATE member_roles SET member_roles.id=member_roles.id+@CNT;

SET @CNT=20000;
UPDATE journals SET journals.id=journals.id+@CNT;
UPDATE journal_details SET journal_details.journal_id=journal_details.journal_id+@CNT;
SET @CNT=30000;
UPDATE journal_details SET journal_details.id=journal_details.id+@CNT;

UPDATE issue_categories SET issue_categories.id=42 where issue_categories.id=1;
UPDATE issues SET issues.category_id=42 where issues.category_id=1;
UPDATE issues SET issues.status_id=2 where issues.status_id=1;
UPDATE issues SET issues.status_id=5 where issues.status_id=8;
UPDATE issues SET issues.status_id=4 where issues.status_id=20;
UPDATE issues SET issues.status_id=20 where issues.status_id=21;

SET @CNT=2000;
UPDATE issue_relations SET issue_relations.id=issue_relations.id+@CNT;

SET @CNT=1000;
UPDATE versions SET versions.id=versions.id+@CNT;
UPDATE issues SET issues.fixed_version_id=issues.fixed_version_id+@CNT;

SET @CNT=10000;
UPDATE watchers SET watchers.id=watchers.id+@CNT;



UPDATE workflows SET workflows.old_status_id=2 where workflows.old_status_id=1;
UPDATE workflows SET workflows.old_status_id=5 where workflows.old_status_id=8;
UPDATE workflows SET workflows.old_status_id=4 where workflows.old_status_id=20;
UPDATE workflows SET workflows.old_status_id=20 where workflows.old_status_id=21;
UPDATE workflows SET workflows.new_status_id=2 where workflows.new_status_id=1;
UPDATE workflows SET workflows.new_status_id=5 where workflows.new_status_id=8;
UPDATE workflows SET workflows.new_status_id=4 where workflows.new_status_id=20;
UPDATE workflows SET workflows.new_status_id=20 where workflows.new_status_id=21;

SET @CNT=5000;
UPDATE workflows SET workflows.id=workflows.id+@CNT;

SET @CNT=60000;
UPDATE custom_values SET custom_values.id=custom_values.id+@CNT;






groups_users 체크(프젝매니저)


delete from groups_users;  
delete from queries;
delete from tokens;
delete from easy_settings;
delete from trackers;
delete from enumerations;  
delete from roles;  
delete from settings;  
delete from schema_migrations;
delete from auth_sources;
delete from boards;
delete from changes;
delete from changeset_parents;
delete from changesets;
delete from changesets_issues;
delete from comments;
delete from custom_field_enumerations;
delete from custom_fields_roles;
delete from documents;
delete from easy_entity_assignments;
delete from import_items;
delete from imports;
delete from messages;
delete from news;
delete from open_id_authentication_associations;
delete from open_id_authentication_nonces;
delete from queries_roles;
delete from repositories;
delete from roles;
delete from roles_managed_roles;
delete from wiki_content_versions;
delete from wiki_pages;
delete from wiki_contents;
delete from wiki_redirects;
delete from wikis;
delete from time_entries;                     
                       
delete from issue_statuses;                               
                  






전제 자동 증가 재 설정 필요

show table status where name='member_roles';
 alter table table_name auto_increment=값;
 
 mysqldump -u root -p --no-create-info database1 > database1.sql
mysqldump -u root -p --no-create-info database2 > database2.sql
mysqldump -u root -p --no-data database1 > schema.sql
새 데이터베이스를 만든 후 다음을 실행하십시오.

mysql -uroot -p -Ddatabase3 < schema.sql
mysql -uroot -p -Ddatabase3 < database1.sql
mysql -uroot -p -Ddatabase3 < database2.sql
