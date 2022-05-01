def filterRequired(simplifiedDict):
    """Filters dictionary and returns the dictionary with only required documents"""

    requiredFields = ['url', 'title', 'description', 'canonical', 'internal_links_count', 'external_links_count',
                      'inbound_links_count', 'images_count', 'title_length', 'description_length', 'cumulative_layout_shift',
                      'plain_text_word_count', 'duplicate_meta_tags', 'og:updated_time', 'article:published_time',
                      'time_to_interactive', 'dom_complete', 'largest_contentful_paint', 'first_input_delay', 'connection_time',
                      'time_to_secure_connection', 'request_sent_time', 'waiting_time', 'download_time', 'duration_time',
                      'fetch_start', 'fetch_end', 'onpage_score', 'broken_resources', 'broken_links', 'duplicate_title',
                      'duplicate_description', 'duplicate_content', 'click_depth', 'high_loading_time', 'is_redirect',
                      'is_4xx_code', 'is_5xx_code', 'is_broken', 'is_www', 'is_https', 'is_http', 'high_waiting_time',
                      'no_h1_tag', 'https_to_http_links', 'size_greater_than_3mb', 'seo_friendly_url',
                      "h1", "h2", "h3", "h4", "h5", "h6"]

    filteredDict = {}

    def filter(simplifiedDict):
        for key in simplifiedDict:
            if key in requiredFields:
                filteredDict[key] = simplifiedDict[key]

        return filteredDict

    return filter(simplifiedDict)
