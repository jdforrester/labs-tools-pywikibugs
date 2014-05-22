channels = {
    "#huggle":
        lambda x: x.get("X-Bugzilla-Product", None) == "Huggle",
    "#pywikibot":
        lambda x: x.get("X-Bugzilla-Product", None) == "Pywikibot",
    "#wikimedia-corefeatures":
        lambda x: (x.get("X-Bugzilla-Product", None) == "MediaWiki extensions") and \
                  (x.get("X-Bugzilla-Component", None) in ["Echo", "Flow", "LiquidThreads", "PageCuration", "Thanks", "WikiLove"]),
    "#wikimedia-dev":
        lambda x: True,
    "#wikimedia-labs":
        lambda x: x.get("X-Bugzilla-Product", None) in ["Tool Labs tools", "Wikimedia Labs"],
    "#wikimedia-mobile":
        lambda x: x.get("X-Bugzilla-Product", None) in ["Wikimedia Mobile", "Commons App", "Wikipedia App", "MobileFrontend"],
    "#wikimedia-qa":
        lambda x: (x.get("X-Bugzilla-Product", None) == "Wikimedia") and \
                  (x.get("X-Bugzilla-Component", None) in ["Continuous integration", "Quality Assurance"]),
    "#mediawiki-feed":
        lambda x: True,
    "#mediawiki-visualeditor":
        lambda x: x.get("X-Bugzilla-Product", None) in ["VisualEditor", "OOjs", "OOjs UI"] or \
                  (
                      (x.get("X-Bugzilla-Product", None) == "MediaWiki extensions") and \
                      (x.get("X-Bugzilla-Component", None) in ["TemplateData"])
                  ),
    "#mediawiki-parsoid":
        lambda x: x.get("X-Bugzilla-Product", None) in ["Parsoid"]
}
