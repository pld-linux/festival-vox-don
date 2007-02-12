Summary:	British English male voice 'Donovan'
Summary(pl.UTF-8):   Brytyjska odmiana języka angielskiego - głos męski 'Donovan'
Name:		festival-vox-don
Version:	0.1
Release:	4
License:	distributable
Group:		Applications/Sound
Source0:	http://www.cstr.ed.ac.uk/download/festival/1.4.2/festvox_don.tar.gz
# Source0-md5:	90442079e34a3a694077f8715d15fbdf
Requires:	festival-lex-OALD
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains data for British English male voice 'Donovan'.
This voice uses a very small and efficient pulse-excited LPC diphone
synthesis method. It was originally written by Steve Isard. The front
end uses the same British English lexicon, intonation and duration
methods as rab_diphone.

%description -l pl.UTF-8
Głos męski "Donovan" dla brytyjskiej odmiany języka angielskiego.
Ten głos używa małej i wydajnej, wzbudzanej impulsami dwugłoskowej
metody syntezy LPC. Oryginalnie był stworzony przez Steve'a Isarda.
Frontend używa tego samego brytyjskiego leksykonu, metod intonacji i
czasów, co rab_diphone.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/festival/lib/voices/english

cd festival/lib/voices/english
cp -r don_diphone $RPM_BUILD_ROOT%{_datadir}/festival/lib/voices/english
rm $RPM_BUILD_ROOT%{_datadir}/festival/lib/voices/english/don_diphone/COPYING

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc festival/lib/voices/english/don_diphone/COPYING
%{_datadir}/festival/lib/voices/english/don_diphone
