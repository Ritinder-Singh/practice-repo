// PROJECT: HTML DSL Builder (Kotlin DSL — Exclusive)
// Goal: enable this syntax:
//   val page = html {
//     head { title { +"My Page" } }
//     body {
//       h1 { +"Hello, World!" }
//       div(id = "content") {
//         p { +"First paragraph" }
//         p { classes("highlight") { +"Second paragraph" } }
//         ul {
//           li { +"Item 1" }
//           li { +"Item 2" }
//         }
//       }
//     }
//   }
//   println(page.render())

// TODO 1: HtmlElement class — holds tag name, attributes, and children
//   class HtmlElement(val tag: String) {
//       val attributes = mutableMapOf<String, String>()
//       val children = mutableListOf<HtmlNode>()
//   }
//   sealed class HtmlNode
//   data class ElementNode(val element: HtmlElement) : HtmlNode()
//   data class TextNode(val text: String) : HtmlNode()

// TODO 2: Builder function pattern
//   fun HtmlElement.element(tag: String, block: HtmlElement.() -> Unit): HtmlElement {
//       val child = HtmlElement(tag).apply(block)
//       children.add(ElementNode(child))
//       return child
//   }

// TODO 3: HTML builder functions
//   fun html(block: HtmlElement.() -> Unit) = HtmlElement("html").apply(block)
//   fun HtmlElement.head(block: HtmlElement.() -> Unit) = element("head", block)
//   fun HtmlElement.body(block: HtmlElement.() -> Unit) = element("body", block)
//   fun HtmlElement.div(id: String? = null, block: HtmlElement.() -> Unit) = element("div", block).also { if (id != null) it.attributes["id"] = id }
//   fun HtmlElement.h1(block: HtmlElement.() -> Unit) = element("h1", block)
//   fun HtmlElement.p(block: HtmlElement.() -> Unit) = element("p", block)
//   fun HtmlElement.ul(block: HtmlElement.() -> Unit) = element("ul", block)
//   fun HtmlElement.li(block: HtmlElement.() -> Unit) = element("li", block)
//   fun HtmlElement.a(href: String, block: HtmlElement.() -> Unit) = element("a", block).also { it.attributes["href"] = href }

// TODO 4: String content via unary plus operator
//   operator fun HtmlElement.unaryPlus(text: String) { children.add(TextNode(text)) }

// TODO 5: CSS class support
//   fun HtmlElement.classes(vararg cls: String, block: HtmlElement.() -> Unit) = element(this.tag, block).also { it.attributes["class"] = cls.joinToString(" ") }

// TODO 6: render() function — recursive with indentation
//   fun HtmlElement.render(indent: Int = 0): String {
//       val pad = "  ".repeat(indent)
//       val attrs = attributes.entries.joinToString("") { """ ${it.key}="${it.value}"""" }
//       val body = children.joinToString("\n") { node ->
//           when (node) {
//               is ElementNode -> node.element.render(indent + 1)
//               is TextNode -> "$pad  ${node.text}"
//           }
//       }
//       return if (body.isEmpty()) "$pad<$tag$attrs/>"
//              else "$pad<$tag$attrs>\n$body\n$pad</$tag>"
//   }

fun main() {
    println("TODO: implement HTML DSL")
}
