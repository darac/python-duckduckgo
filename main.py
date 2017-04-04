from duckduckgo3 import (
    __version__,
    query,
)


def main():
    import sys
    from optparse import OptionParser

    parser = OptionParser(
        usage="usage: %prog [options] query",
        version="ddg3 {}".format(__version__)
    )
    parser.add_option(
        "-o", "--open",
        dest="open",
        action="store_true",
        help="open results in a browser"
    )
    parser.add_option(
        "-n",
        dest="n",
        type="int",
        default=3,
        help="number of results to show"
    )
    parser.add_option(
        "-d",
        dest="d",
        type="int",
        default=None,
        help="disambiguation choice"
    )
    (options, args) = parser.parse_args()
    q = ' '.join(args)

    if options.open:
        import urllib
        import webbrowser

        webbrowser.open(
            "http://duckduckgo.com/?{}".format(
                urllib.urlencode(dict(q=q)),
                new=2
            )
        )

        sys.exit(0)

    results = query(q)

    if options.d and results.type == 'disambiguation':
        try:
            related = results.related[options.d - 1]
        except IndexError:
            print("Invalid disambiguation number.")
            sys.exit(1)
        results = query(related.url.split("/")[-1].replace("_", " "))

    if results.answer and results.answer.text:
        print("Answer: {}\n".format(results.answer.text))
    elif results.abstract and results.abstract.text:
        print("{}\n".format(results.abstract.text))

    if results.type == 'disambiguation':
        print(
            "'{}' can mean multiple things. You can re-run your query "
            "and add '-d #' where '#' is the topic number you're "
            "interested in.\n".format(q)
        )

        for i, related in enumerate(results.related[0:options.n]):
            name = related.url.split("/")[-1].replace("_", " ")
            summary = related.text
            if len(summary) < len(related.text):
                summary += "..."
            print('{}. {}: {}\n'.format(i + 1, name, summary))
    else:
        for i, result in enumerate(results.results[0:options.n]):
            summary = result.text[0:70].replace("&nbsp;", " ")
            if len(summary) < len(result.text):
                summary += "..."
            print("{}. {}".format(i + 1, summary))
            print("  <{}>\n".format(result.url))


if __name__ == '__main__':
    main()
