PROMPT_RTC = """
You are an HTML, CSS expert. And you are well versed in the AI, ML.
I have a model that converts the prompt to html.
I want you to analyze the html code and make a prompt that generate the given html code.
The following is the given html code:
{html}
The following is the example of prompt:
{prompt}
"""


PROMPT_GEN_CONCEPT = """
Generate diverse website layout ideas for different companies, each with a unique design element.
Examples include: a car company site with a left column, a webpage footer with a centered logo.
Explore variations in colors, positions, and company fields. Don’t give any explanations or recognition that you have understood the request, just give the list of 10 ideas, with a line break between
each.
"""


PROMPT_GEN_HTML = """
Code a complete website with a good design in HTML and Tailwind CSS about this: {concept}
Write real and long sentences about the business. NEVER USE sentences starting with Lorem
ipsum, NEVER.
You don’t have to include images, but if you do, use only this source
"https://source.unsplash.com/random/WxH/?keyword", by replacing ‘W‘ and ‘H‘ in the URL
by the desired width and height, and ‘?keyword‘ by a keyword describing the picture, for example
"https://source.unsplash.com/random/300x200/?gym" for an image about gym of size 300x200, or
"https://source.unsplash.com/random/100x200/?cake" for an image of a cake of size 100x200.
"""


PROMPT_MAKE_HTML_COMPLEX = """
You are an HTML, CSS expert. I have an HTML code.
I want you to make the html code more complex.
"""


PROMPT_QUALITY = """
You are an HTML, CSS expert. I have an HTML code.
I want you to evaluate the html code on the following criteria and give a score from 0 to 100.

The following criteria:
1. Semantic HTML: Use appropriate HTML tags to convey meaning. weight: 20
2. Accessibility: Ensure content is usable for all, including those with disabilities. weight: 15
3. Clean and Readable Code: Maintain consistent formatting and meaningful naming conventions. weight: 10
4. Responsive Design: Implement designs that adapt to various screen sizes.  weight: 12
5. Performance Optimization: Minimize file sizes and optimize selectors for faster loading. weight: 10
6. Cross-Browser Compatibility: Ensure consistent rendering across different browsers. weight: 8
7. Validation: Use W3C validators to check for errors and deprecated elements. weight: 7
8. Maintainability: Structure code for easy updates and modifications.  weight: 8
9. Use of Best Practices: Avoid anti-patterns like excessive specificity and inline styles. weight: 5
10. Documentation: Provide clear documentation for styles and design choices. weight: 5

If the html/css code is not following each criteria, reduce score by its weight.

The following is the given html code:
{html}

"""