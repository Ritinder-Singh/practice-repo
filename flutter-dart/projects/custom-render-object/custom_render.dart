import 'package:flutter/rendering.dart';
import 'package:flutter/widgets.dart';

// PROJECT: Custom RenderObject (Exclusive — bypasses widget layer)
// This teaches the lowest level of Flutter's rendering pipeline.
// Add RainbowWidget() to a running Flutter app's widget tree to test.

// TODO 1: Custom RenderBox — draws gradient rainbow stripes
//   class RainbowRenderBox extends RenderBox {
//     @override
//     void performLayout() {
//       size = constraints.biggest;  // take all available space
//     }
//
//     @override
//     void paint(PaintingContext context, Offset offset) {
//       final canvas = context.canvas;
//       final stripeHeight = size.height / 7;
//       final colors = [Colors.red, Colors.orange, Colors.yellow, Colors.green, Colors.blue, Colors.indigo, Colors.violet];
//       for (var i = 0; i < 7; i++) {
//         canvas.drawRect(
//           Rect.fromLTWH(offset.dx, offset.dy + i * stripeHeight, size.width, stripeHeight),
//           Paint()..color = colors[i],
//         );
//       }
//     }
//   }

// TODO 2: LeafRenderObjectWidget — wraps RainbowRenderBox in the widget tree
//   class RainbowWidget extends LeafRenderObjectWidget {
//     const RainbowWidget({super.key});
//
//     @override
//     RenderObject createRenderObject(BuildContext context) => RainbowRenderBox();
//
//     @override
//     void updateRenderObject(BuildContext context, RainbowRenderBox renderObject) {
//       // No properties to update for now
//     }
//   }

// TODO 3: RenderProxyBox — measures child paint time
//   class TimingRenderBox extends RenderProxyBox {
//     @override
//     void paint(PaintingContext context, Offset offset) {
//       final start = DateTime.now();
//       super.paint(context, offset);
//       final elapsed = DateTime.now().difference(start);
//       debugPrint("Paint took: ${elapsed.inMicroseconds}µs");
//     }
//   }
//   class TimingWidget extends SingleChildRenderObjectWidget {
//     const TimingWidget({super.key, super.child});
//     @override
//     RenderObject createRenderObject(BuildContext context) => TimingRenderBox();
//   }

// TODO 4: Multi-child custom layout — manual grid
//   class ManualGridRenderBox extends RenderBox with ContainerRenderObjectMixin<RenderBox, BoxParentData>,
//       RenderBoxContainerDefaultsMixin<RenderBox, BoxParentData> {
//     final int columns;
//     ManualGridRenderBox(this.columns);
//
//     @override
//     void performLayout() {
//       final cellWidth = constraints.maxWidth / columns;
//       var child = firstChild;
//       var row = 0; var col = 0;
//       while (child != null) {
//         child.layout(BoxConstraints.tight(Size(cellWidth, cellWidth)));
//         (child.parentData as BoxParentData).offset = Offset(col * cellWidth, row * cellWidth);
//         col++;
//         if (col >= columns) { col = 0; row++; }
//         child = childAfter(child);
//       }
//       size = Size(constraints.maxWidth, (row + 1) * cellWidth);
//     }
//     @override
//     void paint(PaintingContext context, Offset offset) {
//       defaultPaint(context, offset);
//     }
//   }

// TODO 5: Hit testing
//   @override
//   bool hitTestSelf(Offset position) => size.contains(position);  // this widget captures taps
//   @override
//   bool hitTestChildren(BoxHitTestResult result, {required Offset position}) {
//     return defaultHitTestChildren(result, position: position);
//   }

void main() {
  // Run inside a Flutter app:
  // MaterialApp(home: Scaffold(body: RainbowWidget()))
  print("TODO: add RainbowWidget to a Flutter app's widget tree");
}
