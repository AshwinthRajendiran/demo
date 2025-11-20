// Abstract class Shape
abstract class Shape {
  def area(): Double
}

// Trait to display info
trait DisplayInfo {
  def showInfo(): Unit
}

// Circle subclass
class Circle(val radius: Double) extends Shape with DisplayInfo {
  override def area(): Double = Math.PI * radius * radius

  override def showInfo(): Unit = {
    println(s"Shape: Circle")
    println(s"Radius: $radius")
    println(f"Area: ${area()}%.2f")
  }
}

// Rectangle subclass
class Rectangle(val width: Double, val height: Double) extends Shape with DisplayInfo {
  override def area(): Double = width * height

  override def showInfo(): Unit = {
    println(s"Shape: Rectangle")
    println(s"Width: $width, Height: $height")
    println(f"Area: ${area()}%.2f")
  }
}

// Main object to run program
object ShapeApp {
  def main(args: Array[String]): Unit = {
    val circle = new Circle(5.0)
    val rectangle = new Rectangle(4.0, 6.0)

    println("=== Circle Details ===")
    circle.showInfo()

    println("\n=== Rectangle Details ===")
    rectangle.showInfo()
  }
}