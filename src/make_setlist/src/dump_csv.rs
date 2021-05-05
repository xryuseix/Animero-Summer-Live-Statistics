use csv::Writer;

pub fn dump_csv(
    setlist: &Vec<Vec<String>>,
    filename: String,
) -> Result<(), Box<dyn std::error::Error>> {
    let mut wtr = Writer::from_path(format!("out/{}.csv", filename))?;
    for row in setlist {
        wtr.write_record(row)?;
    }
    wtr.flush()?;
    Ok(())
}
