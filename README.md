# Addresses to Mesh Block Linkset

A linkset formulated using the [Mesh Block Match](http://linked.data.gov.au/def/gnaf/code/MeshBlockMatchTypes) relationship between a [Nov 2018 G-NAF](http://linked.data.gov.au/dataset/gnaf) [Address](http://linked.data.gov.au/def/gnaf#Address) and a [2016 ASGS](http://linked.data.gov.au/dataset/asgs2016) [Mesh Block](http://linked.data.gov.au/def/asgs#MeshBlock).

This Linkset is formulated according to the LocI project's [LocI ontology's Linkset definition](http://linked.data.gov.au/def/loci#Linkset) which extends the [VoID ontology's](https://www.w3.org/TR/void/) *Linkset* definition. LocI Linksets contain both whole-of-Linkset metadata similar to Dataset metadata and additional link information.

## LocI Linksets's additional link information
In addition to VoID Linkset information, LocI Linksets presents some additional per-link information. Where VoID would typically have a link of the form:

```
<DATATASET_A_OBJECT_ID_AA> <PREDICATE_X> <DATASET_B_OBJECT_ID_BB> .
```
showing that `OBJECT_AA` from `DATASET_A` is linked to `OBJECT_BB` from `DATASET_B` via the predicate `PREDICATE_X`, this Linkset, and other LocI Linksets have links of the form:

```
<STATEMENT_ID_N>
  rdf:subject <DATATASET_A_OBJECT_ID_AA> ;
  rdf:predicate <PREDICATE_X> ;
  rdf:object <DATASET_B_OBJECT_ID_BB> ;
  loci:hadGenerationMethod <METHOD_M> .
  dct:created <DATE_CREATED>
```

showing that `OBJECT_AA` is related to `OBJECT_BB` via `PREDICATE_X` but that the relation has an identifier, `STATEMENT_N` allowing it to be directly referenced and any amount of other metadata, such as a reference to the method used to generate this link, in this case `METHOD_M` indicated by the predicate `loci:hadGenerationMethod`.

This is an example of [RDF reification](http://patterns.dataincubator.org/book/reified-statement.html) where a typical RDF relation of a *Subject*, *Predicate* and *Object* is described as an `rdf:Statement` class object with the *Subject*, *Predicate* and *Object* values being indicated by `rdf:subject`, `rdf:predicate` and `rdf:object` properties from the base RDF ontology and other information, such as provenance information, like the reference to the method used to generate the relation here, added to the `rdf:Statement` class just as any RDF information is added to any other class.

## This Linkset's contents
This Linkset consists of the following files:

* **[README.md](README.md)** - This file, providing an introduction to the Linkset
* **[header.ttl](header.ttl)** - An RDF File with metadata about the linkset, and all RDF prefixes used in the linkset.
* **[addrmb16-linkset-10-rows.ttl](addrmb16-linkset-10-rows.ttl)** - An incomplete RDF File showing the first 10 transitiveSfOverlaps relationships used as an example. Turtle format. Not including the header.
* **[addrmb16-linkset-10-rows.csv](addrmb16-linkset-10-rows.csv)** - An incomplete CSV file showing the first 10 rows.
* **[generate_linkset.py](generate_linkset.py)** - The script used to generate the linkset from a CSV file.
* **[linkset_generation_method.txt](linkset_generation_method.txt)** - The generation method for generating the linkset with findings and insights.
* **[query.sql](query.sql)** - The SQL query used to retrieve the CSV data used to generate the linkset. 

## Methods

The method used to generate each link within a Linkset is required by the LocI project's definition of a Linkset to be indicated per-link and this is done so by the `loci:hadGenerationMethod` property. This linkset contains 5 generation methods described by the [Mesh Block Match](http://linked.data.gov.au/def/gnaf/code/MeshBlockMatchTypes).

This linkset's method for generating the linkset is detailed in [linkset_generation_method.txt](linkset_generation_method.txt).

This method may be extracted out of this Linkset in the future and detailed in a stand-alone methods register for better reuse possibilities.


## Rights and License

The content of this API is &copy; [PSMA Australia Limited](https://www.psma.com.au/).

The content is licensed for use under the [Creative Commons 4.0 License](https://creativecommons.org/licenses/by/4.0/). See the [license deed](LICENSE) all details.

## Contacts

*Software Developer*:<br>
**Edmond Chuc**<br>
*Informatics Software Engineer*<br>
CSIRO Land and Water, Environmental Informatics Group<br>
<edmond.chuc@csiro.au><br>
<https://orcid.org/0000-0002-6047-9864><br>

*Project Tech Lead*:<br>
**Nicholas Car**<br>
*Senior Experimental Scientist*<br>
CSIRO Land and Water, Environmental Informatics Group<br>
<nicholas.car@csiro.au><br>
<http://orcid.org/0000-0002-8742-7730>