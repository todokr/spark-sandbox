import Dependencies._

lazy val root = (project in file(".")).
  settings(
    inThisBuild(List(
      organization := "com.example",
      scalaVersion := "2.12.5",
      version      := "0.1.0-SNAPSHOT"
    )),
    name := "Hello",
    libraryDependencies ++= Seq(
      "org.apache.spark" %% "spark-core" % "2.4.0",
      "org.apache.spark" %% "spark-streaming" % "2.4.0",
      scalaTest % Test
    )
  )
